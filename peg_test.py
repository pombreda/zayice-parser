# -*- coding: utf-8 -*-

from parsimonious.grammar import Grammar
'''
grammar = Grammar(
     """
     all_text  = anyChar* bold_text anyChar* 
     anyChar = ~"[A-Z0-9]+"i
     bold_text  = bold_open text bold_close
     text       = ~"[A-Z 0-9]*"i
     bold_open  = "(("
     bold_close = "))"
     """)
'''

definitions = u"""
     wiki_text = wiki_block+
     wiki_block = turkce_section_header / section_content / turkce_wordtype_header / subsection_content / definitions_section  / origin_section  / synonyms_section  / antonyms_section / proverbs_section  / idioms_section / categories_section / template_content / body
     turkce_section_header = section_open "Dil|" non_utf_turkce section_close
     non_utf_turkce = "T" utf_char_replacement "rk" utf_char_replacement "e"
     utf_char_replacement = ~"[^\}]"
     section_content = section_open template_inline section_close
     section_open = "=={{"
     section_close = "}}=="
     turkce_wordtype_header = subsection_open turkce_wordtype_name subsection_close
     turkce_wordtype_name = ~"S[^}]zt[^}]r[^}]\|([^\}]+)"
     subsection_content = subsection_open body subsection_close
     subsection_open = "==={{"
     subsection_close = "}}==="
     definitions_section = template_open "Anlamlar" template_close
     origin_section = template_open ~"K[^}]ken" template_close
     synonyms_section = template_open ~"E[^}] Anlaml[^}]lar" template_close
     antonyms_section = template_open ~"Kar[^}][^}]t Anlaml[^}]lar" template_close
     proverbs_section = template_open ~"Atas[^}]zler" template_close
     idioms_section = template_open "Deyimler" template_close
     categories_section = template_open ~"[^}]st Kavramlar" template_close
     template_content = template_open template_inline template_close
     template_inline = (template_content / body)+
     template_open = "{{"
     template_close = "}}"
     body = ~"[^\{\}]*"
     """

grammar = Grammar(definitions)


test_string = u'{{çekim|may|ı|s}}{{Vikipedi}}{{bakınız|mayıslama}}=={{Dil|Türkçe}}=={{Anlamlar}}:[1] {{t|aylar}} [[yıl|yılın]] 31 [[gün]] süren [[beşinci]] [[ay|ayı]]:{{{{PAGENAME}}}}'
test_string_2 = u"{{çekim|may|ı|s}}{{Vikipedi}}{{bakınız|mayıslama}}=={{Dil|Türkçe}}====={{Söztürü|Ad|Türkçe}}==={{Anlamlar}}:[1] {{t|aylar}} [[yıl|yılın]] 31 [[gün]] süren [[beşinci]] [[ay|ayı]]:[2] taze oy yiyen hayvanlarda olan dışkının cıvık hali{{Söyleniş}}:[[Yardım:Söyleniş|Ses Dosyası]]: {{HP}} [[Media:mayıs.ogg|mayıs]],  ''Çoğul:'' {{HP}}{{Yazılışlar}}:{{Eski Yazı|[[مايس]]}}{{Heceleme}}:ma·yıs, {{çoğul}} ma·yıs·lar{{Kaynaklar}}{{Kaynak-TDK|{{PAGENAME}}}}{{Çeviriler}}{{Üst}}*{{af}}: [1] {{çeviri|af|Mei}}*{{de}}: [1] {{çeviri|de|Mai|m}}, {{çeviri|de|Wonnemond|m}}*{{ar}}: [1] {{çeviri|ar|مَايُو}} (máːyu) m, {{çeviri|ar|أيَّار}}, {{çeviri|ar|مايو}}*{{sq}}: [1] {{çeviri|sq|maj}}*{{ast}}: [1] {{çeviri|ast|mayu}}*{{ay}}: [1] {{çeviri|ay|llamayu}}*{{eu}}: [1] {{çeviri|eu|maiatz}}*{{bs}}: [1] {{çeviri|bs|maj|m}}*{{br}}: [1] {{çeviri|br|Mae}}, {{çeviri|br|miz}} Mae, {{çeviri|br|miz Mae}}*{{bg}}: [1] {{çeviri|bg|май|m}} (maj)*{{rmr}}: [1] {{çeviri|rmr|quindalé}}*{{cs}}: [1] {{çeviri|cs|květen|m}}, {{çeviri|cs|kvìten}}*{{zh}}: [1] {{çeviri|zh|五月}} (wǔyuè)*{{da}}: [1] {{çeviri|da|maj}}*{{id}}: [1] {{çeviri|id|mei}}*{{eo}}: [1] {{çeviri|eo|majo}}*{{et}}: [1] {{çeviri|et|mai}}, {{çeviri|et|maikuu}}, {{çeviri|et|lehekuu}}*{{fo}}: [1] {{çeviri|fo|mai}}*{{fa}}: [1] {{çeviri|fa|می}}*{{fi}}: [1] {{çeviri|fi|toukokuu}}*{{fr}}: [1] {{çeviri|fr|mai|m}}*{{fy}}: [1] {{çeviri|fy|maaie}}, {{çeviri|fy|blommemoanne}}*{{cy}}: [1] {{çeviri|cy|Mai|m}}*{{gl}}: [1] {{çeviri|gl|maio}}*{{gu}}: [1] {{çeviri|gu|મે}}*{{nl}}: [1] {{çeviri|nl|mei}}*{{hr}}: [1] {{çeviri|hr|svibanj}}*{{hi}}: [1] {{çeviri|hi|मई}}*{{io}}: [1] {{çeviri|io|mayo}}*{{he}}: [1] {{çeviri|he|מאי}} (may)*{{en}}: [1] {{çeviri|en|May}}*{{ia}}: [1] {{çeviri|ia|maio}}*{{ga}}: [1] {{çeviri|ga|Bealtaine}}*{{es}}: [1] {{çeviri|es|mayo|m}}{{Orta}}*{{sv}}: [1] {{çeviri|sv|maj}}*{{it}}: [1] {{çeviri|it|maggio}}*{{is}}: [1] {{çeviri|is|maí}}*{{ja}}: [1] {{çeviri|ja|五月}} (ごがつ, {{çeviri|ja|gógatsu)}}*{{ca}}: [1] {{çeviri|ca|maig|m}}*{{qu}}: [1] {{çeviri|qu|aymuray}}*{{ko}}: [1] {{çeviri|ko|오월}} (ovôl)*{{ku}}: [1] {{çeviri|ku|gulan}}*{{la}}: [1] {{çeviri|la|Maius|m}}*{{pl}}: [1] {{çeviri|pl|maj|m}}*{{ln}}: [1] {{çeviri|ln|mai}}*{{lt}}: [1] {{çeviri|lt|gegužė|f}}, {{çeviri|lt|gegužis|m}}, {{çeviri|lt|gegužės mėnuo}}*{{hu}}: [1] {{çeviri|hu|május}}*{{mg}}: [1] {{çeviri|mg|may}}*{{ms}}: [1] {{çeviri|ms|bulan Mei}}, {{çeviri|ms|Mei}}, {{çeviri|ms|مي}}*{{mt}}: [1] {{çeviri|mt|Mejju}}*{{mi}}: [1] {{çeviri|mi|Mei}}*{{mr}}: [1] {{çeviri|mr|मई}}*{{mn}}: [1] {{çeviri|mn|тавдугаар сар}}*{{no}}: [1] {{çeviri|no|mai}}*{{oc}}: [1] {{çeviri|oc|mai}}*{{pt}}: [1] {{çeviri|pt|maio|m}}*{{rap}}: [1] {{çeviri|rap|Ko vai tu\'u potu}}*{{rm}}: [1] {{çeviri|rm|matg}}*{{ro}}: [1] {{çeviri|ro|mai}}*{{ru}}: [1] {{çeviri|ru|май|m}} (maj)*{{sm}}: [1] {{çeviri|sm|Mē}}*{{sa}}: [1] {{çeviri|sa|वैशाखज्येष्ठम्}}*{{sw}}: [1] {{çeviri|sw|Mei}}*{{sr}}: [1] {{çeviri|sr|мај}} (maj)*{{sk}}: [1] {{çeviri|sk|máj|m}}*{{sl}}: [1] {{çeviri|sl|máj}}*{{tl}}: [1] {{çeviri|tl|Mayo}}*{{th}}: [1] {{çeviri|th|พฤษภาคม}} (phriōht sà phaa khohm), {{çeviri|th|เดือนพฤษภาคม}}*{{uk}}: [1] {{çeviri|uk|май|m}} (maj), {{çeviri|uk|травень}}*{{el}}: [1] {{çeviri|el|Μάϊος|m}} (Máïos), {{çeviri|el|Μάιος}}{{Alt}}{{Türk Dilleri}}{{Üst}}*{{az}}: [1] {{çeviri|az|may}}*{{kk}}: [1] {{çeviri|kk|maý}}*{{ky}}: [1] {{çeviri|ky|}}*{{uz}}: [1] {{çeviri|uz|}}{{Orta}}*{{gag}}: {{çeviri|gag|çiçek ay}}*{{tt}}: {{çeviri|tt|maý}}*{{tk}}: {{çeviri|tk|}}{{Alt}}{{Örnekler}}:[2] Oğlum! dikkat et  [[Mayıs]] geldi inekler mayısladı, mayısına basma ayağın kirlenmesin.:[2] Hemşerim, senin [[süt]]ün mayıs kokuyor, [[inek|ineğinin]] [[meme]]lerini güzel yıka, sütün mayıs kokmasın. Çünkü memelerindeki pisliği temizlemediğin mayıs kokuyor.{{Atasözler}}:[1] [[Nisan yağar sap olur, mayıs yağar çeç olur]]{{Köken}}:[1] {{k|Latince}} {{çeviri|la|maius}}{{Yılın ayları}}== {{Dil|Kırım Tatarca}} ===== {{Söztürü|Ad|Kırım Tatarca}} ==={{Anlamlar}}:[1] [[mayıs]]:[2] [[koyun]] pisliği{{Üst Kavramlar}}:[2] [[qoy]] , [[bok]][[af:mayıs]][[ar:mayıs]][[az:mayıs]][[br:mayıs]][[bs:mayıs]][[cs:mayıs]][[da:mayıs]][[de:mayıs]][[el:mayıs]][[en:mayıs]][[es:mayıs]][[eu:mayıs]][[fa:mayıs]][[fi:mayıs]][[fr:mayıs]][[hu:mayıs]][[id:mayıs]][[io:mayıs]][[it:mayıs]][[ko:mayıs]][[lb:mayıs]][[li:mayıs]][[lo:mayıs]][[lt:mayıs]][[mg:mayıs]][[nl:mayıs]][[no:mayıs]][[pl:mayıs]][[pt:mayıs]][[ro:mayıs]][[ru:mayıs]][[sv:mayıs]][[tk:mayıs]][[uz:mayıs]]"
test_string_3 = u"=={{Dil|Türkçe}}====={{Söztürü|Ad|Türkçe}}==='''oğlan''' -nı{{Anlamlar}}:[1] {{t|insansılar}} [[erkek]] [[çocuk]]:[2] [[yetişkin]] erkek:[3] {{t|iskambil}} iskambil kâğıtlarında [[genç]] [[erkek]] [[resim|resimli]] [[kâğıt]]:[4] [[cinsel]] bakımdan erkeklerin [[zevk]]ine [[hizmet]] eden  erkek{{Söyleniş}}:[[Yardım:Söyleniş|Ses Örneği]]: [[Dosya:Tr_tr_oğlan.ogg|thumb]]{{Tireleme}} oğmiddot; lan ''Çoğul'': oğmiddot; lanmiddot; lar{{çekim|oğl|a|n}}{{Köken}}:[1] {{k|Eski Türkçe}} oğ-oğul (küçülmek, küçültmek).{{Eş Anlamlılar}}:[3] [[bacak]], [[vale]]{{Temiz}}{{Atasözler}}:[[Gelin eşikte oğlan beşikte]]:[[Oğlan anası kapı arkası, kız anası minder kabası]]:[[Oğlan atadan öğrenir sofra açmayı, kız anadan öğrenir biçki biçmeyi]]:[[Oğlan dayıya, kız halaya çeker]]:[[Oğlan dayıya,kız halaya çeker]]:[[Oğlan doğur, kız doğur; hamurunu sen yoğur]]:[[Oğlan doğuran övünsün, kız doğuran dövünsün]]{{Kaynaklar}}{{Kaynak-TDK|{{PAGENAME}}}}{{Kaynak-nisanyan|{{PAGENAME}}}}{{Türk Dilleri}}{{Üst}}*{{az}}: {{çeviri|az|oğlan}}*{{krc}}: {{çeviri|krc|ulan}}{{Orta}}*{{tt}}: {{çeviri|tt|malay}}*{{tk}}: {{çeviri|tk|oğlan}}{{Alt}}{{Çeviriler}}{{Üst}}*{{de}}: {{çeviri|de|Junge|m}}, {{çeviri|de|Knabe|m}}*{{ar}}: {{çeviri|ar|وَلَدٌ|m}} (wálad)*{{zh}}: {{çeviri|zh|男孩}} (nánhái)*{{da}}: {{çeviri|da|dreng}}*{{et}}: {{çeviri|et|poiss}}*{{fi}}: {{çeviri|fi|poika}}*{{fr}}: {{çeviri|fr|garcon|m}}*{{nl}}: {{çeviri|nl|jongen|m}}*{{en}}: {{çeviri|en|boy}}*{{es}}: {{çeviri|es|niño|m}}, {{çeviri|es|chico|m}}, {{çeviri|es|muchacho|m}}{{Orta}}*{{sv}}: {{çeviri|sv|pojke}}, {{çeviri|sv|kille}}, {{çeviri|sv|gosse}}*{{it}}: {{çeviri|it|bambino|m}}, {{çeviri|it|ragazzo|m}}*{{ja}}: {{çeviri|ja|男の子}}, {{çeviri|ja|おとこのこ}} (otoko-no-kó), {{çeviri|ja|君}}, {{çeviri|ja|少年}}, {{çeviri|ja|しょうねん}} (shōnen)*{{ko}}: {{çeviri|ko|소년}} (so.nyôn), {{çeviri|ko|남자}} {{çeviri|ko|아이}} (nam.ca a.i), {{çeviri|ko|사내아이}} (sa.nê.a.i), {{çeviri|ko|아이}} (a.i), {{çeviri|ko|꼬마}} (ggo.ma)*{{ku}}: {{çeviri|ku|}}*{{hu}}: {{çeviri|hu|fiú}}, {{çeviri|hu|csávó}}, {{çeviri|hu|srác}}*{{ru}}: {{çeviri|ru|мальчик|m}} (mál’čik), {{çeviri|ru|подросток|m}} (podróstok), {{çeviri|ru|пацан|m}} (patsán)*{{so}}: {{çeviri|so|wiil}}*{{vep}}: {{çeviri|vep|prihaine}}{{Alt}}=={{Dil|Azerice}}====={{Söztürü|Ad|Azerice}}==={{Anlamlar}}:[1] {{t|memeli|akrabalık|dil= Azerice}} [[oğul]], [[oğlan]]=={{Dil|Türkmence}}====={{Söztürü|Ad|Türkmence}}==={{Anlamlar}}:[1] {{t|memeli|akrabalık|dil= Azerice}} [[oğul]], [[oğlan]]:[2] {{t|memeli|akrabalık|dil= Azerice}} [[çocuk]]{{Kaynaklar}}*{{Atacanov, Ata-TYS-1922}}[[af:oğlan]][[az:oğlan]][[de:oğlan]][[el:oğlan]][[en:oğlan]][[fa:oğlan]][[fi:oğlan]][[fj:oğlan]][[fr:oğlan]][[hu:oğlan]][[io:oğlan]][[ka:oğlan]][[ko:oğlan]][[ku:oğlan]][[mg:oğlan]][[pl:oğlan]][[ru:oğlan]][[uz:oğlan]]"

print grammar.parse(test_string_3)

