# python-urlify

This library provides Django's [urlify.js](https://github.com/django/django/blob/master/django/contrib/admin/static/admin/js/urlify.js) functionality ported to Python.

Python 2.7 and 3.3 versions are supported.

Installation:

```shell
pip install -e git+git://github.com/dreikanter/python-urlify#egg=python-urlify
```

Some usage examples:

``` python
from urlify import urlify

urlify('"Fix, Schwyz!" quäkt Jürgen blöd vom Paß')
# 'fix-schwyz-quakt-jurgen-blod-vom-pass'

urlify('Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku')
# 'mulka-hipiji-megina-brivi-nogarsot-celofana-znaudzejcusk'

urlify('Høj bly gom vandt fræk sexquiz på wc.')
# 'hoj-bly-gom-vandt-fraek-sexquiz-pa-wc'

urlify('Чуєш їх, доцю, га? Кумедна ж ти, прощайся без ґольфів!')
# 'chuyesh-yih-docyu-ga-kumedna-zh-ti-proschajsya-bez-golfiv'

urlify('Pack my box with five dozen liquor jugs.')
# 'pack-my-box-five-dozen-liquor-jugs'

urlify('Τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός')
# 'taxisth-alwph3-bafhs-pshmenh-gh-draskelizei-yper-nw8roy-kynos'

urlify('Sveiki pasaulē!')
# 'sveiki-pasaule'

urlify('Pójdźże, kiń tę chmurność w głąb flaszy!')
# 'pojdzze-kin-te-chmurnosc-w-glab-flaszy'

urlify('Příšerně žluťoučký kůň úpěl ďábelské ódy.')
# 'priserne-zlutoucky-kun-upel-dabelske-ody'

urlify('Põdur Zagrebi tšellomängija-följetonist Ciqo külmetas kehvas garaažis')
# 'podur-zagrebi-tsellomangija-foljetonist-ciqo-kulmetas-kehvas-garaazis'

urlify('A grama é amarga')
# 'grama-e-amarga'
```

Alternative implementations:

- https://gist.github.com/Paaskehare/3936118 — a very close implementation to the original JavaScript version.
- https://github.com/wuyuntao/pinyin-urlify — with chinese unicode characters to pinyin convertion.
- https://github.com/beastaugh/urlify — Ruby version.
- [urlify.js](https://github.com/django/django/blob/master/django/contrib/admin/static/admin/js/urlify.js) — original JavaScript implementation released under GNU license.

Copyright &copy; 2013 by [Alex Musayev](http://alex.musayev.com).  
License: [MIT](http://opensource.org/licenses/MIT).  
Project home: [https://github.com/dreikanter/python-urlify](https://github.com/dreikanter/python-urlify).
