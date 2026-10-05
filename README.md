# CEATEC 2026 訪問リスト

CEATEC 2026（10/13–16 幕張メッセ）の出展者に事前にチェックを入れ、ホール別・ブース番号順の訪問プランにまとめるページです。

**ページ:** https://masaohasegawa.github.io/ceatec-visit/

- チェック・訪問済・メモは各自のブラウザ（localStorage）に保存されます。サーバーには送られません。
- 別の端末へは「訪問プラン」タブの引き継ぎコードで移せます。
- 出展者データは [CEATEC 公式 出展者一覧](https://www.ceatec.com/ja/exhibition/exhibitor-list.php) から取得しています。

## データ更新

```
python build.py
```

公式一覧を取り直し、`data.js` と `index.html` / `ceatec-visit.html` を作り直します。
