# Setup

Make journald directory and setup the permission.
```
$ mkdir -p /var/log/journal
$ sudo chmod 777 /var/log/<palworld service name>.log
$ sudo usermod -aG systemd-journal <username>
```

Make sure you installed all requirements.
```
$ pip install -r requirements.txt.
```

Enter the settings.ini file.
```
$ vi settings.ini
```

Run ```$ python run.py```


