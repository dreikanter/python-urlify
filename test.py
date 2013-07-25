# coding: utf-8


from urlify import urlify


TEST = {
    u'"Fix, Schwyz!" quäkt Jürgen blöd vom Paß':
        u'fix-schwyz-quakt-jurgen-blod-vom-pass',

    u'Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku.':
        u'mulka-hipiji-megina-brivi-nogarsot-celofana-znaudzejcusku',

    u'Høj bly gom vandt fræk sexquiz på wc.':
        u'hoj-bly-gom-vandt-fraek-sexquiz-pa-wc',

    u'Чуєш їх, доцю, га? Кумедна ж ти, прощайся без ґольфів!':
        u'chuyesh-yih-docyu-ga-kumedna-zh-ti-proschajsya-bez-golfiv',

    u'Pack my box with five dozen liquor jugs.':
        u'pack-my-box-five-dozen-liquor-jugs',

    u'Τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός':
        u'taxisth-alwph3-bafhs-pshmenh-gh-draskelizei-yper-nw8roy-kynos',

    u'Sveiki pasaulē!':
        u'sveiki-pasaule',

    u'Pójdźże, kiń tę chmurność w głąb flaszy!':
        u'pojdzze-kin-te-chmurnosc-w-glab-flaszy',

    u'Příšerně žluťoučký kůň úpěl ďábelské ódy.':
        u'priserne-zlutoucky-kun-upel-dabelske-ody',

    u'Põdur Zagrebi tšellomängija-följetonist Ciqo külmetas kehvas garaažis':
        u'podur-zagrebi-tsellomangija-foljetonist-ciqo-kulmetas-kehvas-garaazis',

    u'A grama é amarga': u'grama-e-amarga',

    u'': u'',
}


def test():
    for key, value in TEST.items():
        assert(urlify(key) == value)


if __name__ == '__main__':
    test()
