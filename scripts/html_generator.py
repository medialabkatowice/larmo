import yaml

tab_level = 0

def process_(row):
    in_tab()
    print '%s<div class="row">' % tabs()

    for e in row:
        if type(e) == dict:
            c_num = e.keys().pop()

            in_tab()
            if tab_level == 2:
                print '%s<div class="%s columns">' % (tabs(), num_to_word(e.keys().pop(), main=True))
            else:
                print '%s<div class="%s columns">' % (tabs(), num_to_word(e.keys().pop()))

            val   = e.values().pop()
            if type(val) == list:
                process_(val)
            else:
                in_tab()
                print u'%s%s' % (tabs(), parse_(val))
                de_tab()

            print '%s</div>' % tabs()
            de_tab()
        else:
            process_(e)

    print '%s</div>' % tabs()
    de_tab()

def parse_(elem):
    try:
        tag, value = elem.split('|')
    except AttributeError:
        tag, value = '', ''

    tags = {
        'p'   : u'<p>%s</p>' % lorem(),
        'h5'  : u'<h5>%s</h5>' % value,
        'img' : u'<img src="images/%s" />' % value,
        'hr'  : u'<hr />'
    }

    return tags.get(tag, '&nbsp;')

def tabs():
    return '    ' * tab_level

def in_tab():
    global tab_level
    tab_level += 1

def de_tab():
    global tab_level
    tab_level -= 1


def num_to_word(n, main=False):
    nums = [
        '', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'
    ]

    if main:
        result = "main %s" if n == 11 else "help %s"
    else:
        result = "%s"

    return result % nums[n]

def lorem():
    return '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
        ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
        est laborum.'''



if __name__ == '__main__':
    import codecs
    import sys

    fname = sys.argv[1]
    data  = yaml.load(codecs.open(fname, 'r', 'utf-8').read())

    for i, row in enumerate(data):
    	print '<!-- CHAPTER %d -->' % i
        process_(row)