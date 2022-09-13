ガウシアンのAtomlistからcsvfile を作成し、そのファイルからdatfileを作成するプログラム

第一引数は、csvfile の名称( 拡張子なし　)
第二引数は、出力ファイルの名称( 　拡張子なし　)



/*   LinuX環境を想定　*/

gaussianTodat_BSH.py はcutoff のみ


ex)
>>> python3   gaussianTodat.py     example(.csv)    example(.dat)

>>> Enter で実行　　　(最後のデータの時に任意の文字を打ち込む)
>>> 軌道:                   10
>>> on-site:               -17.56

これを繰り返す。

追記
ライブラリpandas が必要なのでinstall する
AtomlistのRows→Select all→file→Export Data→すべての拡張子を選択し「名前.csv」にし、どっかに保存



pandasについて

python3  -m  pip  install  --user  pandas

これでインストールする