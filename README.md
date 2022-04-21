# PDF tools by python
windows PowerShellでPDFの結合がしたくて作った

## 必須環境
- python
- PyPDF4
```
pip install PyPDF4
```

## 使い方
連結したい順番でPDFファイル名を並べる

```-o```で出力ファイル名を指定(.pdfをつけてね)

Power Shell の例
```
python .\pdfmerger.py 'test1.pdf' 'test2.pdf' -o 'out.pdf'
```