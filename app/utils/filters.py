from datetime import datetime


def format_date(date):
    return date.strftime('%m/%d/%y')

# test date formatting
# print(format_date(datetime.now()))


def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


# test URL formatting
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))


def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word


# test plural formatting
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))
