# vgc-stream-debugger
Stream debugger for virtual gimbal camera

If you are using this for the [virtual-gimbal-camera](https://github.com/Clear-Sight/virtual-gimbal-camera) project you will want tom make sure that your **config.json domain** in virtual-gimbal-camera is set to `localhost`.

## install

Do the following commands

Linux, macOS
```bash
git clone git@github.com:Clear-Sight/vgc-stream-debugger.git
cd vgc-stream-debugger/
```
and then
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## run

To start the debugger all you need to do is

```bash
python3 -m debugger
```

When a connection is made a window will appear showing the stream.

If you want to know what the sender needs checkout the file [sender.py](debugger/sender.py)
