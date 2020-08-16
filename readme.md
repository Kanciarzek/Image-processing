## Image Statistics

#### Running app

To run application you must have docker installed. More information: https://www.docker.com/

Download file from: https://bit.ly/2XUmZ5a and put into project directory.

Then you can use command:
```shell script
docker build -t img_stat .
docker run -p 8889:8888 img_stat
```
The part `-p 8889:8888` means forwarding the local port inside container to host port 8889. In this case you will probably receive information:
```
[I 23:14:59.137 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 23:14:59.144 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-7-open.html
    Or copy and paste one of these URLs:
        http://eedf4fad3831:8888/?token=d224dce3a4df069df9fc10564add66cae0fd13d180c2b507
     or http://127.0.0.1:8888/?token=d224dce3a4df069df9fc10564add66cae0fd13d180c2b507

```
Then you need to visit: http://127.0.0.1:8889/?token=d224dce3a4df069df9fc10564add66cae0fd13d180c2b507 with your web browser.

#### Running unit tests

First - you need python 3 (recommended at least python 3.7) and all requirements installed:
```shell script
pip install -r requirements.txt
```
Then you can run tests by:
```shell script
python test.py
```

