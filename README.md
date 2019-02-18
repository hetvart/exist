# Project description

It's a simple spider written with [Scrapy](https://scrapy.org/).
It allows to get and compare car parts info from http://exist.ua
(e.g. prices, delivery dates etc.)

The spider is easy to use. Please perform the below steps to run it:

1. Clone the project and follow the path:
```bash
cd /ProjectPath
```
2. Install all the needed packages from *requirements.txt*:
```bash
pip install -r requirements.txt
```
3. Run the spider using the below command:
```bash
scrapy crawl car_parts -a part_codes={list of part codes separated by comma}

scrapy crawl car_parts -a part_codes="KD5350070,KD4950031A8N,KD5350111,KDY35231XA"
```

The command will gather all the data per every part code and save it to
the project root as json file in a style like the below one:

<details>
<summary>Show/Hide</summary>
<p>

```json
[
  {
    "Brand": "Mazda",
    "Part Code": "KD53-50-070",
    "Part Name": "Кронштейн бампера",
    "Prices": [
      "5103",
      "5351",
      "9683"
    ],
    "Dates": [
      "21.02.2019",
      "20.02.2019",
      "26.02.2019"
    ],
    "Items Available": [
      "4",
      "2",
      "1"
    ]
  },
  {
    "Brand": "Blic",
    "Part Code": "5502-00-3495940P",
    "Part Name": "Усилитель бампера",
    "Prices": [
      "2216"
    ],
    "Dates": [
      "05.03.2019"
    ],
    "Items Available": [
      "10"
    ]
  }
 ]
```

</p>
</details>

That's it!
Enjoy :)
