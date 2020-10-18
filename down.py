from subprocess import PIPE,Popen
from upnload import nload
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

def downloader(update,context,url):
    chat_id = update.message.chat.id
    if msg.startswith('https://vm.tiktok.com') or msg.startswith('https://m.tiktok.com'):
        cmd = [
            "youtube-dl",
            "--no-warnings",
            "j",url]

        s = Popen(cmd,stdout=PIPE,stderr=PIPE)

        stdout, stderr = s.communicate()
        t_response = stdout.decode().strip()
        s.kill()
        if t_response:
            # logger.info(t_response)
            x_reponse = t_response
            if "\n" in x_reponse:
                x_reponse, _ = x_reponse.split("\n")
            response_json = json.loads(x_reponse)
            save_json_path = Config.Dowloadloc+"/"+str(chat_id)+".json"
            with open(save_json_path, "w", encoding="utf8") as outfile:
                json.dump(response_json, outfile, ensure_ascii=False)
            filename = response_json["_filename"]+"mp4"
            caption = response_json["title"]

            comd = [
            "youtube-dl",
            "-c",
            "--hls-prefer-native", url,
            "-o",Config.DOWNLOAD_LOCATION+"/"+filename]

            os.remove(save_json_path)

            j = Popen(comd,stdout=PIPE,stderr=PIPE)
            if stdout or stderr:
                j.kill()
            if stderr:
                update.message.reply_text("An Error occured While Downloading")
                return


            return nload(update,context,Config.DOWNLOAD_LOCATION+"/"+filename,caption)

