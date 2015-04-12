# -*- coding: utf-8 -*-

import unittest
from wiktionaryreader import WiktionaryVisitor

class WiktionaryVisitorTests(unittest.TestCase):

	def getVisitorResult(self, test_string):
		visitor = WiktionaryVisitor()
		visitor.parse(test_string)
		result = visitor.result
		return result

	def testParse(self):
		"Tests if parse method returns a dictionary"
		test_string = ''
		result = self.getVisitorResult(test_string)
		self.assertTrue(type(result) is dict)

	def testSkipNonTurkish(self):
		test_string = u'{{çekim|may|ı|s}}{{Vikipedi}}{{bakınız|mayıslama}}=={{Dil|İngilizce}}=={{Anlamlar}}:[1] {{t|aylar}} [[yıl|yılın]] 31 [[gün]] süren [[beşinci]] [[ay|ayı]]:{{{{PAGENAME}}}}'
		result = self.getVisitorResult(test_string)
		self.assertEqual(len(result), 0)
		test_string = u'{{çekim|may|ı|s}}{{Vikipedi}}{{bakınız|mayıslama}}--=={{Dil|Türkçe}}==--{{Anlamlar}}:[1] {{t|aylar}} [[yıl|yılın]] 31 [[gün]] süren [[beşinci]] [[ay|ayı]]:{{{{PAGENAME}}}}--=={{Dil|İngilizce}}==--{{Anlamlar}}anlam 31'
		result = self.getVisitorResult(test_string)
		self.assertEqual(result['definitions'].count('31'), 1)


	def testReadDefinitions(self):
		test_string = u'{{çekim|may|ı|s}}{{Vikipedi}}{{bakınız|mayıslama}}=={{Dil|Türkçe}}=={{Anlamlar}}:[1] {{t|aylar}} [[yıl|yılın]] 31 [[gün]] süren [[beşinci]] [[ay|ayı]]:{{{{PAGENAME}}}}'
		result = self.getVisitorResult(test_string)
		self.assertTrue('definitions' in result)
		self.assertNotEqual(len(result['definitions']), 0)
		self.assertTrue(result['definitions'].find(u'31') > 0)
		self.assertTrue(result['definitions'].find(u'süren') > 0)
		self.assertFalse(result['definitions'].find(u'PAGENAME') > 0)

	def testReadSynonyms(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|İsim|Türkçe}}==={{Anlamlar}}:[1] [[Bakır]] kapları [[pas]]a ve dış tesirlere karşı korumak üzere [[kalay]] ile kaplayan [[kişi]]{{Eş Anlamlılar}}:[1] [[rassas]][[Kategori:Meslekler]][[en:kalaycı]]'
		result = self.getVisitorResult(test_string)
		self.assertTrue('synoynms' in result)
		self.assertTrue(result['synoynms'].find('rassas') > -1)

	def testReadAntonyms(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|Sıfat|Türkçe}}==={{Anlamlar}}:[1] {{t|dil bilimi}} [[dişi]] [[cins]]ten sayılan, [[müennes]]{{Heceleme}}:{{heceleme|-|di|şil}}{{Eş Anlamlılar}}:[1] [[müennes]]{{Karşıt Anlamlılar}}:[1] [[eril]]{{Çeviriler}}{{Üst}}*{{de}}: {{çeviri|de|feminin}}*{{en}}: {{çeviri|en|feminine}}*{{sv}}: {{çeviri|sv|feminin}}{{Orta}}*{{pt}}: {{çeviri|pt|feminino}}*{{vo}}: {{çeviri|vo|vomik}}{{Alt}}'
		result = self.getVisitorResult(test_string)
		self.assertTrue('antonyms' in result)
		self.assertTrue(result['antonyms'].find('eril') > -1)

	def testReadOrigins(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|İsim|Türkçe}}==={{Anlamlar}}:[1] {{terim|halk ağzı}} {{ağız|Reşadiye}} Doğudan batıya doğru esen, aşırı derecede yakıcı bir soğuk yapan, ocak ayından şubat sonuna kadar esen [[rüzgar]]{{Köken}}:[1] {{k|Eski Türkçe}} [[sarı]] + [[yel]]{{Yan Kavramlar}}:[1] [[sarıyel]], [[karayel]], [[boz yel]], [[kızıl yel]], [[kaba yel]]'
		result = self.getVisitorResult(test_string)
		self.assertTrue('origins' in result)
		self.assertTrue(result['origins'].find(u'sarı') > -1)
		self.assertTrue(result['origins'].find(u'yel') > -1)

	def testProverbs(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|İsim|Türkçe}}==={{Anlamlar}}:[1] {{terim|halk ağzı}} [[şubat|Şubat]]:[2] Yılın ikinci ayı.{{Eş Anlamlılar}}:[[şubat]]{{Atasözler}}:[1] [[Gücük , ya iti soludurum, ya devenin kuyruğuna çıkarım demiş]]'
		result = self.getVisitorResult(test_string)
		self.assertTrue('proverbs' in result)
		self.assertTrue(result['proverbs'].find(u'soludurum') > -1)

	def testIdioms(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|Fiil|Türkçe}}==={{Anlamlar}}:[1] {{terim|halk ağzı|dil=Türkçe}} {{ağız|Sivas}} [[geviş getirmek|Geviş getirmek]]:[2] Sertlik ve gerginliği bozulmak:[3] Yumuşamak, [[yatışmak]], [[sakinleşmek]]:[4] [[çözülmek]]{{Deyimler}}:[[vidaları gevşemek]]{{Türk Dilleri}}{{Üst}}*{{az}}: {{çeviri|az|gövşəmək}}*{{crh}}: {{çeviri|crh|gevşemek}}, {{çeviri|crh|tavsımaq}}*{{tk}}: {{çeviri|tk|govşamak}}*{{etr}}: {{çeviri|tr|seşümek}}*{{etr}}: {{çeviri|tr|mayılmak}}*{{etr}}: {{çeviri|tr|kövremek}}*{{etr}}: {{çeviri|tr|kilfremek}}*{{etr}}: {{çeviri|tr|kevilmek}}*{{etr}}: {{çeviri|tr|kevelmek}}*{{etr}}: {{çeviri|tr|kefremek}}*{{tt}}: {{çeviri|tt|qupşaqlanu}}{{Orta}}{{Alt}}[[ku:gevşemek]][[ky:gevşemek]][[uz:gevşemek]]'
		result = self.getVisitorResult(test_string)
		self.assertTrue('idioms' in result)
		self.assertTrue(result['idioms'].find(u'vidaları gevşemek') > -1)

	def testCategories(self):
		test_string = u'=={{Dil|Türkçe}}====={{Söztürü|İsim|Türkçe}}==={{Anlamlar}}:[1] {{terim|mimarlık}} Düşey ve yanal yüklere karşı dayanımı attırmak üzere [[metal]], [[ahşap]], [[plastik]], [[kompozit]] v.b. sürekli takviye (donatı) elemanlarının yığma örgüsündeki yapı taşları içersine gömülmesi ya da arasına yerleştirilmesi ile [[çatkı|çatkısı]] kurulan çekme, basınç, kayma ve eğilme gerilmeleri oluşturan kuvvetlere karşı dayanımı oldukça arttırılmış bir [[yığma yapım]] biçimi.{{Eş Anlamlılar}}:[1] [[donatılı yığma yapım]]{{Üst Kavramlar}}:[1] [[yığma yapım]]{{Çeviriler}}{{Üst}}*{{en}}: {{çeviri|en|reinforced masonry}}{{Orta}}{{Alt}}'
		result = self.getVisitorResult(test_string)
		self.assertTrue('categories' in result)
		self.assertTrue(result['categories'].find(u'yığma yapım') > -1)		





