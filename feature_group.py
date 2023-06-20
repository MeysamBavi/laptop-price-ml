import csv
import pandas as pd


def feature_in_group(feature, group):
    return any(map(lambda keyword: keyword in feature, group))


def points_of(feature):
    feature = str.lower(feature)
    return tuple([feature_in_group(feature, group) for group in groups])


df = pd.read_csv('./datasets/data.csv', low_memory=False)
features = list(df.columns)

groups = [
    ['ram', 'رم', 'حافظه', 'memory'],
    ['processor', 'cpu', 'پردازنده', 'هسته', 'core', 'پردازش', 'thread', 'رشته', 'ترد'],
    ['disk', 'hard', 'hdd', 'هارد', 'حافظه', 'storage'],
    ['port', 'پورت', 'usb', 'hdmi', 'jack', 'درگاه', 'aux', 'ارتباط', 'دیسک', 'اتصال'],
    ['thunderbolt'],
    ['sd card', 'card'],
    ['cache', 'کش'],
    ['display', 'monitor', 'resolution', 'صفحه', 'رزولوشن', 'نمایش', 'تصویر', 'نمايش', 'تصوير'],
    ['graphic', 'gpu', 'گرافیک', 'vga'],
    ['battery', 'باتری', 'باطری', 'باتري', 'باطري', 'شارژ', 'voltage'],
    ['country', 'کشور'],
    ['brand', 'سري', 'سری', 'سازنده', 'series', 'شرکت', 'مدل'],
    ['wifi', 'wireless', 'شبکه', 'وایرلس', 'وايرلس'],
    ['camera', 'دوربین', 'دوربين', 'webcam', 'وبکم'],
    ['size', 'dimension', 'ابعاد', 'ضخامت'],
    ['weight', 'وزن', 'گرم'],
    ['speaker', 'اسپیکر', 'اسپيکر', 'بلندگو', 'بلند گو'],
    ['os', 'operating system', 'سیستم عامل', 'سيستم عامل'],
    ['gaming', 'گیمینگ', 'گيمينگ', 'بازی', 'بازي', 'game'],
    ['keyboard', 'کیبورد', 'کيبورد', 'کلید', 'کليد'],
    ['refresh', 'رفرش', 'رسانی', 'رساني'],
    ['color', 'رنگ'],
]


features = sorted(features)
features = sorted(features, key=points_of, reverse=True)

with open('./datasets/features.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['feature-name', 'example-1', 'example-2', 'example-3'])
    writer.writeheader()
    for f in features:
        values = df[f].dropna()
        examples = list(values.iloc[:2])
        if len(values) > 2:
            examples.append(values.iloc[-1])
        e1 = examples[0] if len(examples) > 0 else ''
        e2 = examples[1] if len(examples) > 1 else ''
        e3 = examples[2] if len(examples) > 2 else ''
        writer.writerow({
            'feature-name': f,
            'example-1': e1,
            'example-2': e2,
            'example-3': e3
        })
