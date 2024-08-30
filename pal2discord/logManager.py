import subprocess
import re

class logManager:
    def __init__(self, log_path, svc_name):
        self.log_path = log_path + svc_name + '.log'
        self.svc_name = svc_name
        

    def get_last_journal_entry(self):
        #最新のログエントリを取得
        result = subprocess.run(
            ['journalctl', '-u', f'{self.svc_name}.service', '--no-pager', '-n', '1'],
            stdout=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()


    def get_last_log_line(self):
        #ログファイルの最後の行を取得
        try:
            with open(self.log_path, 'rb') as f:
                f.seek(0, 2)  # ファイルの終端に移動
                file_size = f.tell()
                if file_size == 0:
                    return ''

                # 最後の改行文字を探す
                buffer_size = 1024
                buffer = b''
                offset = min(file_size, buffer_size)

                while offset > 0:
                    f.seek(-offset, 2)
                    buffer = f.read(min(buffer_size, file_size))
                    if b'\n' in buffer:
                        break
                    offset += buffer_size

                last_line = buffer.splitlines()[-1].decode()
                return last_line

        except FileNotFoundError:
            return ''


    def append_log_entry(self, entry):
        #新しいログエントリをログファイルに追加
        with open(self.log_path, 'a') as f:
            f.write(entry + '\n')


    def get_latest_pal_chat(self):
        # journalctlから最新のログエントリを取得
        latest_entry = self.get_last_journal_entry()

        # ログファイルの最後の行を取得
        last_log_line = self.get_last_log_line()

        # ログが異なる場合のみログファイルを更新
        if latest_entry != last_log_line:
            self.append_log_entry(latest_entry)
            
            match = re.search(r'\[(CHAT|LOG)\](.*)', latest_entry)
            if match:
                ch = match.group(2).strip()

                if 'joined the server.' in ch:
                    ch = ch.split('joined the server.')[0].strip() + ' がログインしました！'
                elif 'left the server.' in ch:
                    ch = ch.split('left the server.')[0].strip() + ' がログアウトしました！'
                elif 'connected the server.' in ch:
                    return
                elif 'REST accessed endpoint /v1/api/' in ch:
                    return
                else:
                    pass

                print(ch)
                return ch
                 
            else:
                # マッチしなかった場合はNoneを返す
                return None
