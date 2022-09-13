1.概要
　バンド計算をしたlogfileからバンド図を作るプログラム

2.中身
　データ取得
　↓
　valence orbital 数・conduction orbital 数　取得
　↓
　エネルギの表を作成　%ここでエクセルファイル出力もありだと思います
　↓
　可視化

3.使いかた
　filename.log のバンド図を描きたいとき

　$ python autoband.py  filename

matplotlibが入ってなかったら

python3  -m  pip  install  --user  matplotlib

これでインストールする