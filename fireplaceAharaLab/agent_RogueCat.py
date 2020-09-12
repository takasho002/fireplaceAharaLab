# agent_RogueCat.py

import random

from hearthstone.enums import CardClass, CardType, Race
from utils import ExceptionPlay, Candidate, executeAction, getCandidates
from agent_Standard import postAction

#from agent_RogueCat import printAllRogueCards
def printAllRogueCards():
	from fireplace import cards
	#cards.db.initialize()
	collection = []
	for card in cards.db.keys():
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [CardClass.ROGUE, CardClass.NEUTRAL]:# Play with more possibilities
			continue
		collection.append(cls)
	for card in collection:
		dscrpt = card.description
		if '断末魔' in dscrpt:
			print("			elif ID in {'%s'}:"%(card.id))
			print("				cond1.append(['deathrattle','', ''])")
			print("				#%s : %s"%(card.name, card.description.replace('\n','')))
	return collection

def RogueCatAI(game, option=[], debugLog=False):
	while True:
		myCandidate = getCandidates(game)
		if len(myCandidate)>0:
			myChoice = random.choice(myCandidate)
			executeAction(thisgame, myChoice, debugLog=debugLog)
			postAction(player)
		else:
			return

def haveDragon(game):
	return False


def RogueCat_Condition(game, card, target):
	cond1=[]#満たしている条件
	cond2=[]#効果
	dscrpt = card.description.replace('\n','')
	player = game.current_player
	myHeroHealth=player.hero.health
	hisHeroHealth=player.opponent.hero.health
	myTauntH = 0
	myMinionH = 0
	myAttack = 0
	for card in player.characters:
		if card.can_attack():
			myAttack += card.atk
		if card.taunt:
			myTauntH += card.health
		if card.type == CardType.MINION:
			myMinionH += card.health
	hisTauntH = 0
	hisAttack = 0
	for card in player.opponent.characters:
		if card.can_attack():
			hisAttack += card.atk
		if card. taunt:
			hisTauntH += card.ahealth
	myHeroRemainder=myHeroHealth+myTaunt-hisAttack
	hisHeroRemainder=hisHeroHealth+hisTaunt-myAttack
	myMinionRemainder=myMinionHealth
	ID = card.id
	if '激励' in dscrpt:#ヒーローパワーを使うと発動する
		#基本的にいつでもあとまわし。内容によっては場との関連がありうる。
		pass
	if '突撃' in dscrpt:#すぐに攻撃できるcharge
		if  card.charge:
			if ID in {'AT_070'}:
				cond1.append(['charge', 'myRemainder<hisRemainder', 'lessConst'])
			elif ID in {'AT_125', 'UNG_099'}:
				cond1.append(['charge', 'myRemainder<hisRemainder', 'noAttack'])
			elif ID in {'EX1_116'}:
				cond1.append(['charge', 'myRemainder<hisRemainder', 'summon'])
			elif ID in {'CS2_146'}:
				if player.hero.weapon != None:
					cond1.append(['charge', 'myRemainder<hisRemainder', None])
			elif ID in {'CS2_124', 'AT_087', 'CS2_131', 'CS2_171', 'CS2_213', 'EX1_062', 'EX1_067', 'GVG_098'}:
				cond1.append(['charge', 'myRemainder<hisRemainder', None])
		pass
	elif '断末魔' in dscrpt:#死ぬときに発動 deathrattle
		#基本的にいつでも。内容によっては場との関連がありうる。
		#断末魔を召喚したり追加したりするカードも基本的にいつでもOK
		#相手ミニオンに力があり、出してもすぐに殺されることがわかっているときは優先。
			if ID in {'AT_036'}:
				cond1.append(['deathrattle','', 'summon'])
				#アヌバラク : [x]<b>断末魔:</b>このカードを自分の手札に戻し4/4のネルビアン1体を[x]召喚する。
			elif ID in {'AT_123'}:
				cond1.append(['deathrattle','haveDragon()', 'damageAll'])
				#チルモー : [x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。
			elif ID in {'AT_128'}:
				cond1.append(['deathrattle','', 'backCardHand'])
				#骸骨騎士 : [x]<b>断末魔:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、このミニオンを自分の手札に戻す。
			elif ID in {'BOT_031'}:
				cond1.append(['deathrattle','', 'damage'])
				#ゴブリン爆弾 : [x]<b>断末魔:</b>敵のヒーローに___2ダメージを与える。
			elif ID in {'BOT_066'}:
				cond1.append(['deathrattle','', 'summon'])
				#メカ・チビドラゴン : [x]<b>断末魔:</b>7/7の「メカ・ドラゴン」を__1体召喚する。
			elif ID in {'BOT_084'}:
				cond1.append(['deathrattle','', 'addCardHand'])
				#紫の煙霧 : [x]<b>断末魔</b>を持つランダムなカード2枚を自分の手札に追加する。
			elif ID in {'BOT_102'}:
				cond1.append(['deathrattle','', 'addCardHand'])
				#スパーク・ドリル : [x]<b>急襲</b><b>断末魔:</b><b>急襲</b>を持つ1/1の「スパーク」2体を自分の手札に追加する。
			elif ID in {'BOT_267'}:
				cond1.append(['deathrattle','', 'summon'])
				#手動操縦のリーパー : [x]<b>断末魔:</b>自分の手札からコスト（2）以下のランダムなミニオンを1体召喚する。
			elif ID in {'BOT_286'}:
				cond1.append(['deathrattle','', 'help'])
				#ネクリウムの刃 : [x]<b>断末魔:</b>ランダムな味方のミニオン1体の____<b>断末魔</b>を発動する。
			elif ID in {'BOT_312'}:
				cond1.append(['deathrattle','', 'summon'])
				#自己増殖型メナス : [x]<b>超電磁</b><b>断末魔:</b>1/1の「マイクロロボ」を3体召喚する。
			elif ID in {'BOT_401'}:
				cond1.append(['deathrattle','', 'addCardHand'])
				#兵器化ピニャータ : [x]<b>断末魔:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の_____手札に追加する。
			elif ID in {'BOT_424'}:
				cond1.append(['deathrattle','noDeck() and noHand() and noCharacter()', 'damageHero'])
				#メックトゥーン : [x]<b>断末魔:</b>自分のデッキ、手札、陣地にカードがない場合_____敵のヒーローを破壊する。
			elif ID in {'BOT_445'}:
				cond1.append(['deathrattle','', 'summon'])
				#メカンガルー : [x]<b>断末魔:</b>1/1の「コメカンガルー」を1体召喚する。
			elif ID in {'BOT_508'}:
				cond1.append(['deathrattle','', 'help'])
				#ネクリウムの小瓶 : [x]味方のミニオン1体の<b>断末魔</b>を___2回発動させる。
			elif ID in {'BOT_565'}:
				cond1.append(['deathrattle','', 'summon'])
				#ブライトノズル・クローラー : <b>断末魔:</b><b>猛毒</b>と<b>急襲</b>を持つ1/1のウーズを1体召喚する。
			elif ID in {'BOT_606'}:
				cond1.append(['deathrattle','heHasMinion()', 'damage'])
				#ブーマーロボ : <b>断末魔:</b>ランダムな敵のミニオン1体に__4ダメージを与える。
			elif ID in {'BOT_700'}:
				cond1.append(['deathrattle','', 'summon'])
				#チョッキンガー : <b>超電磁</b>、<b>木霊</b><b>断末魔:</b>1/1の「マイクロロボ」を2体召喚する。
			elif ID in {'BRM_027'}:
				cond1.append(['deathrattle','', 'changeHero'])
				#筆頭家老エグゼクタス : [x]<b>断末魔:</b>自分のヒーローを「炎の王ラグナロス」と置き換える。
			elif ID in {'BT_008'}:
				cond1.append(['deathrattle','', 'summon'])
				#錆鉄の入門者 : [x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。
			elif ID in {'BT_126'}:
				cond1.append(['deathrattle','', 'summon'])
				#テロン・ゴアフィーンド : [x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。
			elif ID in {'BT_155'}:
				cond1.append(['deathrattle','', 'summon'])
				#屑鉄山のコロッサス : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。
			elif ID in {'BT_160'}:
				cond1.append(['deathrattle','', 'help'])
				#錆鉄の狂信者 : [x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。
			elif ID in {'BT_703'}:
				cond1.append(['deathrattle','', 'summon'])
				#呪われた流れ者 : [x]<b>断末魔:</b><b>隠れ身</b>を持つ7/5の影を1体召喚する。
			elif ID in {'BT_713'}:
				cond1.append(['deathrattle','', 'addCardDeck'])
				#アカマ : [x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。
			elif ID in {'BT_726'}:
				cond1.append(['deathrattle','', 'summon'])
				#ドラゴンモーの飛行追跡者 : <b>断末魔:</b>3/4の「ドラゴンライダー」を1体召喚する。
			elif ID in {'BT_728'}:
				cond1.append(['deathrattle','', 'summon'])
				#顔を隠した放浪者 : <b>断末魔:</b>9/1の審問官を1体召喚する。
			elif ID in {'BT_735'}:
				cond1.append(['deathrattle','', 'summon'])
				#アラール : [x]<b>断末魔</b>:0/3の「アラールの灰」を1体召喚する。次の自分のターンに灰は___「アラール」に変身する。
			elif ID in {'CFM_095'}:
				cond1.append(['deathrattle','', 'addCardHisDeck'])
				#穴掘りイタチ : [x]<b>断末魔:</b> このミニオンを相手のデッキに混ぜる。
			elif ID in {'CFM_120'}:
				cond1.append(['deathrattle','', 'restoreBoth'])
				#超うざい調剤師 : [x]<b>断末魔:</b>各ヒーローの体力を#4回復する。
			elif ID in {'CFM_341'}:
				cond1.append(['deathrattle','heHasMinion()', 'damage'])
				#サリー巡査部長 : <b>断末魔:</b>敵のミニオン全てにこのミニオンの攻撃力に等しいダメージを与える。
			elif ID in {'CFM_646'}:
				cond1.append(['deathrattle','', 'damage'])
				#裏町のレプラノーム : [x]<b>断末魔:</b>敵のヒーローに____2ダメージを与える。
			elif ID in {'CFM_667'}:
				cond1.append(['deathrattle','heHasMinion()', 'damage'])
				cond1.append(['deathrattle','', 'damageSelf'])
				#爆弾部隊 : [x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。
			elif ID in {'CFM_691'}:
				cond1.append(['deathrattle','', 'summon'])
				#翡翠の鎌刀 : [x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
			elif ID in {'CFM_902'}:
				cond1.append(['deathrattle','', 'summon'])
				#アヤ・ブラックポー : [x]<b>雄叫び＆断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び＆断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
			elif ID in {'DAL_088'}:
				cond1.append(['deathrattle','', 'summon'])
				#金庫番 : <b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。
			elif ID in {'DAL_566'}:
				cond1.append(['deathrattle','', 'summon'])
				#奇抜な書記官 : [x]<b>断末魔:</b>1/1の「息巻く巻物」を4体召喚する。
			elif ID in {'DAL_720'}:
				cond1.append(['deathrattle','', 'backCardHand'])
				#ワグル・ピック : [x]<b>断末魔:</b>ランダムな味方のミニオン1体を自分の手札に戻す。そのミニオンのコストは（2）減る。
			elif ID in {'DAL_743'}:
				cond1.append(['deathrattle','', 'summon'])
				#ヘンチ・クランの騎豚 : [x]<b>急襲</b>、<b>断末魔:</b>1/1のマーロックを1体召喚する。
			elif ID in {'DAL_749'}:
				cond1.append(['deathrattle','card.atk>=4', 'summon'])
				#神出鬼没の怪人 : [x]<b>断末魔:</b>このミニオンの攻撃力が4以上の場合__再度召喚する。
			elif ID in {'DAL_775'}:
				cond1.append(['deathrattle','', 'damageAll'])
				#トンネル爆破係 : [x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。
			elif ID in {'DRG_036'}:
				cond1.append(['deathrattle','', 'summon'])
				#ワクサドレッド : [x]<b>断末魔:</b>引かれた際「ワクサドレッド」を再度召喚するロウソク1枚を______自分のデッキに混ぜる。_
			elif ID in {'DRG_049'}:
				cond1.append(['deathrattle','haveDragon()', 'help'])
				#美味しいマロバルーン : <b>断末魔:</b>自分の手札のドラゴン1体に__+2/+2を付与する。
			elif ID in {'DRG_071'}:
				cond1.append(['deathrattle','', 'addSmallCardHisDeck'])
				#悪運アホウドリ : [x]<b>断末魔:</b>相手のデッキに1/1の「アホウドリ」2体を混ぜる。
			elif ID in {'DRG_086'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#クロマティックの卵 : [x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！
			elif ID in {'EX1_012'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#ブラッドメイジ・サルノス : [x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。
			elif ID in {'EX1_016'}:
				cond1.append(['deathrattle','', 'getMinion'])
				#シルヴァナス・ウィンドランナー : [x]<b>断末魔:</b>ランダムな敵のミニオン1体を味方にする。
			elif ID in {'EX1_029'}:
				cond1.append(['deathrattle','', 'damage'])
				#レプラノーム : [x]<b>断末魔:</b> 敵のヒーローに　2ダメージを与える。
			elif ID in {'EX1_096'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#戦利品クレクレ君 : [x]<b>断末魔:</b>カードを1枚引く。
			elif ID in {'EX1_097'}:
				cond1.append(['deathrattle','', 'damageAll'])
				#涜れしもの : [x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。
			elif ID in {'EX1_110'}:
				cond1.append(['deathrattle','', 'summon'])
				#ケーアン・ブラッドフーフ : [x]<b>断末魔:</b>4/5のベイン・ブラッドフーフを1体召喚する。
			elif ID in {'EX1_556'}:
				cond1.append(['deathrattle','', 'summon'])
				#刈入れゴーレム : [x]<b>断末魔:</b> 2/1の壊れかけのゴーレムを1体召喚する。
			elif ID in {'EX1_577'}:
				cond1.append(['deathrattle','', 'summonHisMion'])
				#魔獣 : [x]<b>断末魔:</b> 3/3のフィンクル・アインホルンを1体敵の陣地に召喚する。
			elif ID in {'FP1_001'}:
				cond1.append(['deathrattle','myHeroMaxHealth>myHeroHealth', 'restore'])
				#エサゾンビ : [x]<b>断末魔:</b>敵のヒーローの体力を#5回復する。
			elif ID in {'FP1_002'}:
				cond1.append(['deathrattle','', 'summon'])
				#呪われた蜘蛛 : <b>断末魔:</b> 1/1の亡霊蜘蛛を2体召喚する。
			elif ID in {'FP1_004'}:
				cond1.append(['deathrattle','', 'addCardDeck'])
				#マッドサイエンティスト : [x]<b>断末魔:</b> 自分のデッキにある_______<b>秘策</b>1枚を準備する。
			elif ID in {'FP1_007'}:
				cond1.append(['deathrattle','', 'summon'])
				#ネルビアンの卵 : <b>断末魔:</b> 4/4のネルビアンを1体召喚する。
			elif ID in {'FP1_009'}:
				cond1.append(['deathrattle','', ''])
				#デスロード : [x]<b>挑発、断末魔:</b> 相手プレイヤーはデッキからミニオン_______1体を陣地に置く。_
			elif ID in {'FP1_012'}:
				cond1.append(['deathrattle','', ''])
				#ヘドロゲッパー : [x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。
			elif ID in {'FP1_014'}:
				cond1.append(['deathrattle','', ''])
				#スタラグ : <b>断末魔:</b> この対戦中にフューゲンも死亡した場合、サディアスを召喚する。
			elif ID in {'FP1_015'}:
				cond1.append(['deathrattle','', ''])
				#フューゲン : [x]<b>断末魔:</b> この対戦中にスタラグも死亡していた場合____サディアスを召喚する。
			elif ID in {'FP1_024'}:
				cond1.append(['deathrattle','', ''])
				#不安定なグール : [x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。
			elif ID in {'FP1_026'}:
				cond1.append(['deathrattle','', ''])
				#アヌバー・アンブッシャー : [x]<b>断末魔:</b> ランダムな味方のミニオン1体を_______自分の手札に戻す。_
			elif ID in {'FP1_028'}:
				cond1.append(['deathrattle','', ''])
				#墓掘り人 : [x]自分が<b>断末魔</b>を持つミニオンを召喚する度__攻撃力+1を獲得する。
			elif ID in {'FP1_029'}:
				cond1.append(['deathrattle','', ''])
				#踊る剣 : [x]<b>断末魔:</b>相手はカードを1枚引く。
			elif ID in {'FP1_031'}:
				cond1.append(['deathrattle','', ''])
				#バロン・リーヴェンデア : [x]味方のミニオンの__<b>断末魔</b>は2回発動する。
			elif ID in {'GIL_118'}:
				cond1.append(['deathrattle','', ''])
				#キジル博士 : [x]<b>断末魔:</b>自分のヒーローの体力を#8回復する。
			elif ID in {'GIL_513'}:
				cond1.append(['deathrattle','', ''])
				#迷える魂 : <b>断末魔:</b>味方のミニオン全てに攻撃力+1を__付与する。
			elif ID in {'GIL_557'}:
				cond1.append(['deathrattle','', ''])
				#呪われた漂流者 : [x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。
			elif ID in {'GIL_578'}:
				cond1.append(['deathrattle','', ''])
				#アッシュモア伯爵夫人 : [x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。
			elif ID in {'GIL_614'}:
				cond1.append(['deathrattle','', ''])
				#ヴードゥー人形 : [x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。
			elif ID in {'GIL_616'}:
				cond1.append(['deathrattle','', ''])
				#裂けるフェスタールート : [x]<b>断末魔:</b>2/2の「裂けた若木」を2体召喚する。
			elif ID in {'GIL_667'}:
				cond1.append(['deathrattle','', ''])
				#朽ちかけたアップルバウム : [x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。
			elif ID in {'GIL_816'}:
				cond1.append(['deathrattle','', ''])
				#沼のドラゴンの卵 : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
			elif ID in {'GVG_076'}:
				cond1.append(['deathrattle','', ''])
				#爆発ヒツジ : <b>断末魔:</b> 全てのミニオンに2ダメージを与える。
			elif ID in {'GVG_078'}:
				cond1.append(['deathrattle','', ''])
				#メカ・イェティ : <b>断末魔:</b> 各プレイヤーに<b>スペアパーツ</b>カード1枚を与える。
			elif ID in {'GVG_082'}:
				cond1.append(['deathrattle','', ''])
				#ゼンマイ仕掛けのノーム : <b>断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
			elif ID in {'GVG_096'}:
				cond1.append(['deathrattle','', ''])
				#手動操縦のシュレッダー : <b>断末魔:</b> ランダムなコスト2のミニオン1体を召喚する。
			elif ID in {'GVG_097'}:
				cond1.append(['deathrattle','', ''])
				#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
			elif ID in {'GVG_105'}:
				cond1.append(['deathrattle','', ''])
				#手動操縦のスカイ・ゴーレム : <b>断末魔:</b> ランダムなコスト4のミニオン1体を召喚する。
			elif ID in {'GVG_114'}:
				cond1.append(['deathrattle','', ''])
				#スニードの旧型シュレッダー : <b>断末魔:</b> ランダムな<b>レジェンド</b>のミニオン1体を召喚する。
			elif ID in {'GVG_115'}:
				cond1.append(['deathrattle','', ''])
				#トッシュリー : [x]<b>雄叫び、断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
			elif ID in {'ICC_019'}:
				cond1.append(['deathrattle','', ''])
				#骸骨術師 : [x]<b>断末魔:</b>今が相手のターンの場合8/8のスケルトンを1体召喚する。
			elif ID in {'ICC_025'}:
				cond1.append(['deathrattle','', ''])
				#ガラガラガイコツ : [x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。
			elif ID in {'ICC_027'}:
				cond1.append(['deathrattle','', ''])
				#ボーン・ドレイク : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
			elif ID in {'ICC_065'}:
				cond1.append(['deathrattle','', ''])
				#ボーン・バロン : <b>断末魔:</b>1/1のスケルトン2体を自分の手札に追加する。
			elif ID in {'ICC_067'}:
				cond1.append(['deathrattle','', ''])
				#ヴライグール : [x]<b>断末魔:</b>今が相手のターンの場合2/2のグールを1体召喚する。
			elif ID in {'ICC_098'}:
				cond1.append(['deathrattle','', ''])
				#墓に潜むもの : [x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。

			elif ID in {'ICC_099'}:
				cond1.append(['deathrattle','', ''])
				#涜れし爆弾 : <b>断末魔:</b>味方のミニオン全てに5ダメージを与える。
			elif ID in {'ICC_201'}:
				cond1.append(['deathrattle','', ''])
				#骰は投げられた : [x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。
			elif ID in {'ICC_257'}:
				cond1.append(['deathrattle','', ''])
				#死体蘇生者 : [x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。
			elif ID in {'ICC_702'}:
				cond1.append(['deathrattle','', ''])
				#浅めの墓穴堀り : <b>断末魔:</b><b>断末魔</b>を持つランダムなミニオン1体を自分の手札に追加する。
			elif ID in {'ICC_812'}:
				cond1.append(['deathrattle','', ''])
				#ミートワゴン : [x]<b>断末魔:</b>このミニオンより攻撃力が低いミニオンを1体自分のデッキから召喚する。
			elif ID in {'ICC_854'}:
				cond1.append(['deathrattle','', ''])
				#アーファス : <b>断末魔:</b>ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。
			elif ID in {'KAR_029'}:
				cond1.append(['deathrattle','', ''])
				#ルーンの卵 : <b>断末魔:</b>カードを1枚引く。
			elif ID in {'KAR_041'}:
				cond1.append(['deathrattle','', ''])
				#堀に潜むもの : <b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。
			elif ID in {'KAR_094'}:
				cond1.append(['deathrattle','', ''])
				#殺意のフォーク : <b>断末魔:</b>3/2の武器1枚を自分の手札に追加する。
			elif ID in {'LOE_012'}:
				cond1.append(['deathrattle','', ''])
				#墓荒らし : <b>断末魔:</b> 自分の手札に「コイン」1枚を追加する。
			elif ID in {'LOE_019'}:
				cond1.append(['deathrattle','', ''])
				#掘り起こされたラプター : [x]<b>雄叫び:</b> 味方のミニオン1体を選択する。そのミニオンの____<b>断末魔</b>の能力をコピーする。
			elif ID in {'LOE_046'}:
				cond1.append(['deathrattle','', ''])
				#巨大ガマ : <b>断末魔:</b> ランダムな敵1体に1ダメージを与える。
			elif ID in {'LOE_061'}:
				cond1.append(['deathrattle','', ''])
				#アヌビサス・センチネル : [x]<b>断末魔:</b>ランダムな味方のミニオン1体に____+3/+3を付与する。
			elif ID in {'LOE_089'}:
				cond1.append(['deathrattle','', ''])
				#ふらつくこびと達 : <b>断末魔:</b> 2/2のこびとを3体召喚する。
			elif ID in {'LOOT_144'}:
				cond1.append(['deathrattle','', ''])
				#護宝のドラゴン : [x]<b>断末魔:</b>相手に「コイン」2枚を与える。
			elif ID in {'LOOT_153'}:
				cond1.append(['deathrattle','', ''])
				#ヴァイオレット・ヴルム : <b>断末魔:</b>1/1の「芋虫」を7体召喚する。
			elif ID in {'LOOT_161'}:
				cond1.append(['deathrattle','', ''])
				#肉食キューブ : [x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。
			elif ID in {'LOOT_184'}:
				cond1.append(['deathrattle','', ''])
				#シルバーヴァンガード : [x]<b>断末魔:</b>コスト8のミニオンを1体<b>招集</b>する。
			elif ID in {'LOOT_233'}:
				cond1.append(['deathrattle','', ''])
				#呪われた門弟 : [x]<b>断末魔:</b>5/1のレヴナントを1体召喚する。
			elif ID in {'LOOT_412'}:
				cond1.append(['deathrattle','', ''])
				#コボルトの幻術師 : [x]<b>断末魔:</b>自分の手札からミニオン1体の1/1のコピーを1体召喚する。
			elif ID in {'LOOT_413'}:
				cond1.append(['deathrattle','', ''])
				#装甲虫 : <b>断末魔:</b>装甲を3獲得する。
			elif ID in {'LOOT_503'}:
				cond1.append(['deathrattle','', ''])
				#オニキスの小呪文石 : [x]ランダムな敵のミニオン1体を破壊する。@<i>（<b>断末魔</b>カードを3枚手札から使用するとアップグレード）</i>
			elif ID in {'LOOT_542'}:
				cond1.append(['deathrattle','', ''])
				#大逆の刃キングスベイン : 付与された効果を常に維持する。<b>断末魔:</b>この武器を自分のデッキに混ぜる。
			elif ID in {'OG_072'}:
				cond1.append(['deathrattle','', ''])
				#地の底の探索 : <b>断末魔</b>を持つカード1枚を<b>発見</b>する。
			elif ID in {'OG_080'}:
				cond1.append(['deathrattle','', ''])
				#蠱毒なザリル : [x]<b>雄叫び＆断末魔:</b> ランダムな毒素カード1枚を自分の手札に追加する。
			elif ID in {'OG_133'}:
				cond1.append(['deathrattle','', ''])
				#頽廃させしものン＝ゾス : <b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。
			elif ID in {'OG_147'}:
				cond1.append(['deathrattle','', ''])
				#狂闘品のヒールロボ : [x]<b>断末魔:</b>敵のヒーローの体力を#8回復する。
			elif ID in {'OG_151'}:
				cond1.append(['deathrattle','', ''])
				#ン＝ゾスの触手 : <b>断末魔:</b> 全てのミニオンに1ダメージを与える。
			elif ID in {'OG_158'}:
				cond1.append(['deathrattle','', ''])
				#熱く教えを乞うもの : <b>断末魔:</b> ランダムな味方のミニオン1体に+1/+1を付与する。
			elif ID in {'OG_249'}:
				cond1.append(['deathrattle','', ''])
				#蝕まれしトーレン : [x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。
			elif ID in {'OG_256'}:
				cond1.append(['deathrattle','', ''])
				#ン＝ゾスの落とし子 : [x]<b>断末魔:</b>味方のミニオン全てに+1/+1を付与する。
			elif ID in {'OG_267'}:
				cond1.append(['deathrattle','', ''])
				#南海のスキッドフェイス : [x]<b>断末魔:</b> 自分の武器に___攻撃力+2を付与する。
			elif ID in {'OG_272'}:
				cond1.append(['deathrattle','', ''])
				#黄昏の鎚の召喚師 : <b>断末魔:</b> 5/5の無貌の破壊者を1体召喚する。
			elif ID in {'OG_317'}:
				cond1.append(['deathrattle','', ''])
				#竜王デスウィング : [x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。
			elif ID in {'OG_323'}:
				cond1.append(['deathrattle','', ''])
				#汚染利品グログロ君 : <b>断末魔:</b> カードを1枚引く。
			elif ID in {'OG_330'}:
				cond1.append(['deathrattle','', ''])
				#アンダーシティの押し売り : [x]<b>断末魔:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
			elif ID in {'SCH_162'}:
				cond1.append(['deathrattle','', ''])
				#ヴェクタス : [x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。
			elif ID in {'SCH_426'}:
				cond1.append(['deathrattle','', ''])
				#潜入者リリアン : [x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。
			elif ID in {'SCH_707'}:
				cond1.append(['deathrattle','', ''])
				#空を翔けるトビウオ : [x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。
			elif ID in {'SCH_708'}:
				cond1.append(['deathrattle','', ''])
				#日陰草の非行生徒 : [x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。
			elif ID in {'SCH_709'}:
				cond1.append(['deathrattle','', ''])
				#イキってる四年生 : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。
			elif ID in {'SCH_711'}:
				cond1.append(['deathrattle','', ''])
				#疫病始祖ドレイク : [x]<b>断末魔:</b>ランダムなコスト7のミニオン1体を召喚する。
			elif ID in {'SCH_714'}:
				cond1.append(['deathrattle','', ''])
				#英才エレク : [x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
			elif ID in {'TRL_074'}:
				cond1.append(['deathrattle','', ''])
				#ギザギザの歯 : [x]<b>断末魔:</b>味方のミニオン全てに<b>急襲</b>を付与する。
			elif ID in {'TRL_363'}:
				cond1.append(['deathrattle','', ''])
				#サロナイト鉱山の奴隷監督 : [x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。
			elif ID in {'TRL_409'}:
				cond1.append(['deathrattle','', ''])
				#サメのロア・グラル : [x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。
			elif ID in {'TRL_503'}:
				cond1.append(['deathrattle','', ''])
				#スカラベの卵 : [x]<b>断末魔:</b>1/1の「スカラベ」を3体召喚する。
			elif ID in {'TRL_505'}:
				cond1.append(['deathrattle','', ''])
				#ひ弱なヒナ : <b>断末魔:</b>自分の手札の獣1体のコストを（1）減らす。
			elif ID in {'TRL_520'}:
				cond1.append(['deathrattle','', ''])
				#マーロック・テイスティーフィン : [x]<b>断末魔:</b>自分のデッキから__マーロックを2体引く。
			elif ID in {'TRL_525'}:
				cond1.append(['deathrattle','', ''])
				#闘技場の宝箱 : <b>断末魔:</b>カードを2枚引く。
			elif ID in {'TRL_531'}:
				cond1.append(['deathrattle','', ''])
				#ランブルタスク・シェイカー : [x]<b>断末魔:</b>3/2の「ランブルタスク・ブレイカー」を1体召喚する。
			elif ID in {'TRL_537'}:
				cond1.append(['deathrattle','', ''])
				#ダ・アンダテイカ : [x]<b>雄叫び:</b>この対戦で死亡した味方のミニオン3体の_____<b>断末魔</b>を獲得する。_
			elif ID in {'TRL_541'}:
				cond1.append(['deathrattle','', ''])
				#魂剥ぐロア・ハッカー : [x]<b>断末魔:</b>各プレイヤーのデッキに「ケガレた血」を1枚ずつ混ぜる。
			elif ID in {'ULD_174'}:
				cond1.append(['deathrattle','', 'summon'])
				#ヘビの卵 : <b>断末魔:</b>3/4の「シーサーペント」を1体召喚する。
			elif ID in {'ULD_177'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#オクトサリ : <b>断末魔:</b>カードを8枚引く。
			elif ID in {'ULD_183'}:
				cond1.append(['deathrattle','', 'help'])
				#アヌビサス・ウォーブリンガー : <b>断末魔:</b>自分の手札のミニオン全てに+3/+3を付与する。
			elif ID in {'ULD_184'}:
				cond1.append(['deathrattle','', 'damage'])
				#コボルトのサンドトルーパー : [x]<b>断末魔:</b>敵のヒーローに___3ダメージを与える。
			elif ID in {'ULD_208'}:
				cond1.append(['deathrattle','', 'restore'])
				#カルトゥートの守護者 : [x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。
			elif ID in {'ULD_250'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#虫食いゴブリン : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。
			elif ID in {'ULD_280'}:
				cond1.append(['deathrattle','', 'backCardHisHand'])
				#サーケットの昏倒強盗 : <b>断末魔:</b>ランダムな敵のミニオン1体を___相手の手札に戻す。
			elif ID in {'ULD_282'}:
				cond1.append(['deathrattle','', 'DrawCard'])
				#壺の商人 : [x]<b>断末魔:</b>ランダムなコスト1のミニオン1体を____自分の手札に追加する。
			elif ID in {'ULD_706'}:
				cond1.append(['deathrattle','', 'summon'])
				#バレバレの囮 : [x]<b>断末魔:</b>各プレイヤーは手札の最もコストが低いミニオンを1体召喚する。
			elif ID in {'UNG_010'}:
				cond1.append(['deathrattle','', 'summon'])
				#満腹のスレッシャドン : [x]<b>断末魔:</b>1/1のマーロックを3体召喚する。
			elif ID in {'UNG_065'}:
				cond1.append(['deathrattle','', 'asleep'])
				#死体花シェラジン : [x]<b>断末魔:</b><b>休眠状態</b>になる。1ターン中に4枚のカードを手札から使用すると______このミニオンは復活する。_
			elif ID in {'UNG_076'}:
				cond1.append(['deathrattle','', 'summon'])
				#卵泥棒 : [x]<b>断末魔:</b>1/1のラプターを2体召喚する。
			elif ID in {'UNG_083'}:
				cond1.append(['deathrattle','', 'summon'])
				#デビルサウルスの卵 : [x]<b>断末魔:</b>5/5のデビルサウルスを1体召喚する。
			elif ID in {'UNG_818'}:
				cond1.append(['deathrattle','', 'damage'])
				#即発のエレメンタル : <b>断末魔:</b>ランダムな敵のミニオン1体に　3ダメージを与える。
			elif ID in {'UNG_845'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#火成のエレメンタル : [x]<b>断末魔:</b>1/2のエレメンタル2体を自分の手札に追加する。
			elif ID in {'UNG_900'}:
				cond1.append(['deathrattle','', 'help'])
				#霊の歌い手ウンブラ : 自分がミニオンを召喚した後そのミニオンの<b>断末魔</b>を発動する。
			elif ID in {'YOD_016'}:
				cond1.append(['deathrattle','', 'drawCard'])
				#飛掠船員 : <b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。




			if ID in {'AT_128','FP1_026','DAL_720'}:
				cond1.append(['deathrattle',(),'backToHand'])
			if ID in {'BRM_027'}:
				cond1.append(['deathrattle',(),'changeHero'])
			if ID in {'AT_123'}:
				if haveDragon():
					cond1.append(['deathrattle',(),'damageBoth'])
			if ID in {'BOT_606', 'BOT_031','CFM_341','CFM_646','EX1_029','GIL_614','ULD_184','UNG_818'}:
				cond1.append(['deathrattle',(),'damage'])
			if ID in {'DAL_775','EX1_097','FP1_024','GVG_076','LOE_046','OG_151'}:
				cond1.append(['deathrattle',(),'damageBoth'])
			if ID in {'CFM_667','ICC_099','CFM_667'}:
				cond1.append(['deathrattle',(),'damageSelf'])

			if ID in {'BT_713','BOT_102','BOT_401','UNG_845','ULD_282','ULD_250','ULD_177','TRL_525','TRL_520','TRL_409','SCH_709','SCH_708','SCH_707','OG_330','OG_323','OG_080','LOOT_184','LOE_012','KAR_094','KAR_029','ICC_854','ICC_702','ICC_065','DRG_086','EX1_012','EX1_096','FP1_004','GIL_816','GVG_082','GVG_115','ICC_027'}:
				cond1.append(['deathrattle',(),'drawCard'])
			if ID in {'BOT_286','BOT_508'}:
				cond1.append(['deathrattle',(),'help'])
			if ID in {'DAL_749'}:
				if card.health>=4:
					cond1.append(['deathrattle',(),'summon'])
			if ID in {'AT_036','BOT_066','BOT_267','BOT_312','BOT_445','BOT_565','BOT_700','BT_008','BT_126','BT_155','BT_703','BT_726','BT_728','BT_735','CFM_691','CFM_902','DAL_088','DAL_566',\
			'DRG_036','EX1_016','EX1_110','EX1_556','FP1_002','FP1_007','FP1_012','FP1_014','FP1_015','GIL_616','GVG_096','GVG_105','GVG_114','ICC_019','ICC_025',\
			'ICC_067','ICC_812','KAR_041','LOE_089','LOOT_153','LOOT_161','LOOT_233','LOOT_412','OG_133','OG_249','OG_272','SCH_162','SCH_711',\
			'TRL_363','TRL_503','TRL_531','ULD_174','ULD_706','UNG_010','UNG_076','UNG_083','DAL_743'}:
				cond1.append(['deathrattle',(),'summon'])
			if ID in {'BOT_084'}:
				cond1.append(['drawCard',True, 'deathrattle'])
			if ID in {'FP1_028'}:
				cond1.append(['restore',(),'deathrattle'])




			if ID in {'CFM_095'}:
				cond1.append(['deathrattle',(),'addHisDeck'])
			if ID in {'CFM_120'}:
				cond1.append(['deathrattle',(),'restoreBoth'])
			if ID in {'DRG_049'}:
				if haveDragon():
					cond1.append(['deathrattle',(),'restore'])
			if ID in {'DRG_071'}:
				cond1.append(['deathrattle',(),'addHisDeck'])
			if ID in {'EX1_577'}:
				cond1.append(['deathrattle',(),'summonOpponent'])
			if ID in {'FP1_001'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'FP1_009'}:
				cond1.append(['deathrattle',(),'playHisCard'])
			if ID in {'FP1_029'}:
				cond1.append(['deathrattle',(),'drawHisCard'])
			if ID in {'GIL_118'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'GIL_513'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'GIL_557'}:
				cond1.append(['deathrattle',(),()])################ drawCard
				#呪われた漂流者 : [x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。
			if ID in {'GIL_667'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#沼のドラゴンの卵 : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
			if ID in {'GVG_078'}:
				cond1.append(['deathrattle',(),'drawCardBoth'])
				#メカ・イェティ : <b>断末魔:</b> 各プレイヤーに<b>スペアパーツ</b>カード1枚を与える。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#ゼンマイ仕掛けのノーム : <b>断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#トッシュリー : [x]<b>雄叫び、断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#ボーン・ドレイク : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#ボーン・バロン : <b>断末魔:</b>1/1のスケルトン2体を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#浅めの墓穴堀り : <b>断末魔:</b><b>断末魔</b>を持つランダムなミニオン1体を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#アーファス : <b>断末魔:</b>ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#ルーンの卵 : <b>断末魔:</b>カードを1枚引く。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#殺意のフォーク : <b>断末魔:</b>3/2の武器1枚を自分の手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#墓荒らし : <b>断末魔:</b> 自分の手札に「コイン」1枚を追加する。
			if ID in {'LOE_061'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'LOOT_144'}:
				cond1.append(['deathrattle',(),'drawHisCard'])
				#護宝のドラゴン : [x]<b>断末魔:</b>相手に「コイン」2枚を与える。
			if ID in {}:
				cond1.append(['deathrattle',(),'drawCard'])
				#シルバーヴァンガード : [x]<b>断末魔:</b>コスト8のミニオンを1体<b>招集</b>する。
			if ID in {'LOOT_413'}:
				if player.weapon != None:
					cond1.append(['deathrattle',(),'restore'])
			if ID in {'LOOT_542'}:
				cond1.append(['deathrattle',(),'addCardDeck'])
				#大逆の刃キングスベイン : 付与された効果を常に維持する。<b>断末魔:</b>この武器を自分のデッキに混ぜる。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#蠱毒なザリル : [x]<b>雄叫び＆断末魔:</b> ランダムな毒素カード1枚を自分の手札に追加する。
			if ID in {'OG_147'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'OG_158'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'OG_256'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {'OG_267'}:
				if player.weapon != None:
					cond1.append(['deathrattle',(),'restore'])
			if ID in {'OG_317'}:
				cond1.append(['deathrattle',(),'playCard'])
				#竜王デスウィング : [x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#汚染利品グログロ君 : <b>断末魔:</b> カードを1枚引く。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#アンダーシティの押し売り : [x]<b>断末魔:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
			if ID in {'SCH_426'}:
				cond1.append(['deathrattle',(),'summon'])
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#空を翔けるトビウオ : [x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#日陰草の非行生徒 : [x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#イキってる四年生 : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。
			if ID in {'SCH_714'}:
				cond1.append(['deathrattle',(),'addCardDeck'])
				#英才エレク : [x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
			if ID in {'TRL_074'}:
				if HaveMinion():
					cond1.append(['deathrattle',(),'restore'])
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#サメのロア・グラル : [x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。
			if ID in {'TRL_505'}:
				cond1.append(['deathrattle',(),'help'])
				#ひ弱なヒナ : <b>断末魔:</b>自分の手札の獣1体のコストを（1）減らす。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#マーロック・テイスティーフィン : [x]<b>断末魔:</b>自分のデッキから__マーロックを2体引く。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#闘技場の宝箱 : <b>断末魔:</b>カードを2枚引く。
			if ID in {'TRL_541'}:
				cond1.append(['deathrattle',(),'addCardDeck'])
				#魂剥ぐロア・ハッカー : [x]<b>断末魔:</b>各プレイヤーのデッキに「ケガレた血」を1枚ずつ混ぜる。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#オクトサリ : <b>断末魔:</b>カードを8枚引く。
			if ID in {'ULD_183'}:
				cond1.append(['deathrattle',(),'restore'])
				#アヌビサス・ウォーブリンガー : <b>断末魔:</b>自分の手札のミニオン全てに+3/+3を付与する。
			if ID in {'ULD_208'}:
				cond1.append(['deathrattle',(),'restore'])
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#虫食いゴブリン : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。
			if ID in {'ULD_280'}:
				cond1.append(['deathrattle','','backCardHisHand'])
				#サーケットの昏倒強盗 : <b>断末魔:</b>ランダムな敵のミニオン1体を___相手の手札に戻す。
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#壺の商人 : [x]<b>断末魔:</b>ランダムなコスト1のミニオン1体を____自分の手札に追加する。
			if ID in {'ULD_288'}:
				cond1.append(['deathrattle',(),()])
				#斂葬のアンカ : [x]<b>雄叫び:</b>自分の手札の<b>断末魔</b>を持つ各ミニオンをそれぞれコスト（1）の1/1に変える。
			if ID in {'UNG_065'}:
				cond1.append(['deathrattle',(),()])
				#死体花シェラジン : [x]<b>断末魔:</b><b>休眠状態</b>になる。1ターン中に4枚のカードを手札から使用すると______このミニオンは復活する。_
			if ID in {}:
				cond1.append(['deathrattle',(),()])
				#火成のエレメンタル : [x]<b>断末魔:</b>1/2のエレメンタル2体を自分の手札に追加する。
			if ID in {'YOD_016'}:
				cond1.append(['deathrattle',(),()])
				#飛掠船員 : <b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。
	
#[AT_036][アヌバラク]([x]<b>断末魔:</b>このカードを自分の手札に戻し4/4のネルビアン1体を[x]召喚する。)
#[AT_123][チルモー]([x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。)
#[AT_128][骸骨騎士]([x]<b>断末魔:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、このミニオンを自分の手札に戻す。)
#[BOT_031][ゴブリン爆弾]([x]<b>断末魔:</b>敵のヒーローに___2ダメージを与える。)
#[BOT_066][メカ・チビドラゴン]([x]<b>断末魔:</b>7/7の「メカ・ドラゴン」を__1体召喚する。)
#[BOT_084][紫の煙霧]([x]<b>断末魔</b>を持つランダムなカード2枚を自分の手札に追加する。)
#[BOT_102][スパーク・ドリル]([x]<b>急襲</b><b>断末魔:</b><b>急襲</b>を持つ1/1の「スパーク」2体を自分の手札に追加する。)
#[BOT_243][マイラ・ロットスプリング]([x]<b>雄叫び:</b><b>断末魔</b>を持つミニオンを1体<b>発見</b>する。さらにそのミニオンの__<b>断末魔</b>を獲得する。)
#[BOT_267][手動操縦のリーパー]([x]<b>断末魔:</b>自分の手札からコスト（2）以下のランダムなミニオンを1体召喚する。)
#[BOT_286][ネクリウムの刃]([x]<b>断末魔:</b>ランダムな味方のミニオン1体の____<b>断末魔</b>を発動する。)
#[BOT_312][自己増殖型メナス]([x]<b>超電磁</b><b>断末魔:</b>1/1の「マイクロロボ」を3体召喚する。)
#[BOT_401][兵器化ピニャータ]([x]<b>断末魔:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の_____手札に追加する。)
#[BOT_424][メックトゥーン]([x]<b>断末魔:</b>自分のデッキ、手札、陣地にカードがない場合_____敵のヒーローを破壊する。)
#[BOT_445][メカンガルー]([x]<b>断末魔:</b>1/1の「コメカンガルー」を1体召喚する。)
#[BOT_508][ネクリウムの小瓶]([x]味方のミニオン1体の<b>断末魔</b>を___2回発動させる。)
#[BOT_565][ブライトノズル・クローラー](<b>断末魔:</b><b>猛毒</b>と<b>急襲</b>を持つ1/1のウーズを1体召喚する。)
#[BOT_606][ブーマーロボ](<b>断末魔:</b>ランダムな敵のミニオン1体に__4ダメージを与える。)
#[BOT_700][チョッキンガー](<b>超電磁</b>、<b>木霊</b><b>断末魔:</b>1/1の「マイクロロボ」を2体召喚する。)
#[BRM_027][筆頭家老エグゼクタス]([x]<b>断末魔:</b>自分のヒーローを「炎の王ラグナロス」と置き換える。)
#[BT_008][錆鉄の入門者]([x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。)
#[BT_126][テロン・ゴアフィーンド]([x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。)
#[BT_155][屑鉄山のコロッサス]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。)
#[BT_160][錆鉄の狂信者]([x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。)
#[BT_703][呪われた流れ者]([x]<b>断末魔:</b><b>隠れ身</b>を持つ7/5の影を1体召喚する。)
#[BT_713][アカマ]([x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。)
#[BT_726][ドラゴンモーの飛行追跡者](<b>断末魔:</b>3/4の「ドラゴンライダー」を1体召喚する。)
#[BT_728][顔を隠した放浪者](<b>断末魔:</b>9/1の審問官を1体召喚する。)
#[BT_735][アラール]([x]<b>断末魔</b>:0/3の「アラールの灰」を1体召喚する。次の自分のターンに灰は___「アラール」に変身する。)
#[CFM_095][穴掘りイタチ]([x]<b>断末魔:</b> このミニオンを相手のデッキに混ぜる。)
#[CFM_120][超うざい調剤師]([x]<b>断末魔:</b>各ヒーローの体力を#4回復する。)
#[CFM_341][サリー巡査部長](<b>断末魔:</b>敵のミニオン全てにこのミニオンの攻撃力に等しいダメージを与える。)
#[CFM_646][裏町のレプラノーム]([x]<b>断末魔:</b>敵のヒーローに____2ダメージを与える。)
#[CFM_667][爆弾部隊]([x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。)
#[CFM_691][翡翠の鎌刀]([x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_855][デファイアスの掃除屋]([x]<b>雄叫び:</b><b>断末魔</b>を持つミニオン1体を<b>沈黙</b>させる。)
#[CFM_902][アヤ・ブラックポー]([x]<b>雄叫び＆断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び＆断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[DAL_088][金庫番](<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。)
#[DAL_566][奇抜な書記官]([x]<b>断末魔:</b>1/1の「息巻く巻物」を4体召喚する。)
#[DAL_720][ワグル・ピック]([x]<b>断末魔:</b>ランダムな味方のミニオン1体を自分の手札に戻す。そのミニオンのコストは（2）減る。)
#[DAL_743][ヘンチ・クランの騎豚]([x]<b>急襲</b>、<b>断末魔:</b>1/1のマーロックを1体召喚する。)
#[DAL_749][神出鬼没の怪人]([x]<b>断末魔:</b>このミニオンの攻撃力が4以上の場合__再度召喚する。)
#[DAL_775][トンネル爆破係]([x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。)
#[DRG_031][ネクリウムの薬師]([x]<b>コンボ:</b>自分のデッキから<b>断末魔</b>を持つミニオンを1体引きその<b>断末魔</b>を獲得する。)
#[DRG_036][ワクサドレッド]([x]<b>断末魔:</b>引かれた際「ワクサドレッド」を再度召喚するロウソク1枚を______自分のデッキに混ぜる。_)
#[DRG_049][美味しいマロバルーン](<b>断末魔:</b>自分の手札のドラゴン1体に__+2/+2を付与する。)
#[DRG_071][悪運アホウドリ]([x]<b>断末魔:</b>相手のデッキに1/1の「アホウドリ」2体を混ぜる。)
#[DRG_086][クロマティックの卵]([x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！)
#[EX1_012][ブラッドメイジ・サルノス]([x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。)
#[EX1_016][シルヴァナス・ウィンドランナー]([x]<b>断末魔:</b>ランダムな敵のミニオン1体を味方にする。)
#[EX1_029][レプラノーム]([x]<b>断末魔:</b> 敵のヒーローに　2ダメージを与える。)
#[EX1_096][戦利品クレクレ君]([x]<b>断末魔:</b>カードを1枚引く。)
#[EX1_097][涜れしもの]([x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。)
#[EX1_110][ケーアン・ブラッドフーフ]([x]<b>断末魔:</b>4/5のベイン・ブラッドフーフを1体召喚する。)
#[EX1_556][刈入れゴーレム]([x]<b>断末魔:</b> 2/1の壊れかけのゴーレムを1体召喚する。)
#[EX1_577][魔獣]([x]<b>断末魔:</b> 3/3のフィンクル・アインホルンを1体敵の陣地に召喚する。)
#[FP1_001][エサゾンビ]([x]<b>断末魔:</b>敵のヒーローの体力を#5回復する。)
#[FP1_002][呪われた蜘蛛](<b>断末魔:</b> 1/1の亡霊蜘蛛を2体召喚する。)
#[FP1_004][マッドサイエンティスト]([x]<b>断末魔:</b> 自分のデッキにある_______<b>秘策</b>1枚を準備する。)
#[FP1_007][ネルビアンの卵](<b>断末魔:</b> 4/4のネルビアンを1体召喚する。)
#[FP1_009][デスロード]([x]<b>挑発、断末魔:</b> 相手プレイヤーはデッキからミニオン_______1体を陣地に置く。_)
#[FP1_012][ヘドロゲッパー]([x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。)
#[FP1_014][スタラグ](<b>断末魔:</b> この対戦中にフューゲンも死亡した場合、サディアスを召喚する。)
#[FP1_015][フューゲン]([x]<b>断末魔:</b> この対戦中にスタラグも死亡していた場合____サディアスを召喚する。)
#[FP1_024][不安定なグール]([x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。)
#[FP1_026][アヌバー・アンブッシャー]([x]<b>断末魔:</b> ランダムな味方のミニオン1体を_______自分の手札に戻す。_)
#[FP1_028][墓掘り人]([x]自分が<b>断末魔</b>を持つミニオンを召喚する度__攻撃力+1を獲得する。)
#[FP1_029][踊る剣]([x]<b>断末魔:</b>相手はカードを1枚引く。)
#[FP1_031][バロン・リーヴェンデア]([x]味方のミニオンの__<b>断末魔</b>は2回発動する。)
#[GIL_118][キジル博士]([x]<b>断末魔:</b>自分のヒーローの体力を#8回復する。)
#[GIL_513][迷える魂](<b>断末魔:</b>味方のミニオン全てに攻撃力+1を__付与する。)
#[GIL_557][呪われた漂流者]([x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。)
#[GIL_578][アッシュモア伯爵夫人]([x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。)
#[GIL_614][ヴードゥー人形]([x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。)
#[GIL_616][裂けるフェスタールート]([x]<b>断末魔:</b>2/2の「裂けた若木」を2体召喚する。)
#[GIL_667][朽ちかけたアップルバウム]([x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。)
#[GIL_816][沼のドラゴンの卵]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[GVG_076][爆発ヒツジ](<b>断末魔:</b> 全てのミニオンに2ダメージを与える。)
#[GVG_078][メカ・イェティ](<b>断末魔:</b> 各プレイヤーに<b>スペアパーツ</b>カード1枚を与える。)
#[GVG_082][ゼンマイ仕掛けのノーム](<b>断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。)
#[GVG_096][手動操縦のシュレッダー](<b>断末魔:</b> ランダムなコスト2のミニオン1体を召喚する。)
#[GVG_097][リトル・エクソシスト]([x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_)
#[GVG_105][手動操縦のスカイ・ゴーレム](<b>断末魔:</b> ランダムなコスト4のミニオン1体を召喚する。)
#[GVG_114][スニードの旧型シュレッダー](<b>断末魔:</b> ランダムな<b>レジェンド</b>のミニオン1体を召喚する。)
#[GVG_115][トッシュリー]([x]<b>雄叫び、断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。)
#[ICC_019][骸骨術師]([x]<b>断末魔:</b>今が相手のターンの場合8/8のスケルトンを1体召喚する。)
#[ICC_025][ガラガラガイコツ]([x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。)
#[ICC_027][ボーン・ドレイク]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[ICC_065][ボーン・バロン](<b>断末魔:</b>1/1のスケルトン2体を自分の手札に追加する。)
#[ICC_067][ヴライグール]([x]<b>断末魔:</b>今が相手のターンの場合2/2のグールを1体召喚する。)
#[ICC_098][墓に潜むもの]([x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。)
#[ICC_099][涜れし爆弾](<b>断末魔:</b>味方のミニオン全てに5ダメージを与える。)
#[ICC_201][骰は投げられた]([x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。)
#[ICC_257][死体蘇生者]([x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。)
#[ICC_702][浅めの墓穴堀り](<b>断末魔:</b><b>断末魔</b>を持つランダムなミニオン1体を自分の手札に追加する。)
#[ICC_812][ミートワゴン]([x]<b>断末魔:</b>このミニオンより攻撃力が低いミニオンを1体自分のデッキから召喚する。)
#[ICC_854][アーファス](<b>断末魔:</b>ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。)
#[KAR_029][ルーンの卵](<b>断末魔:</b>カードを1枚引く。)
#[KAR_041][堀に潜むもの](<b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。)
#[KAR_094][殺意のフォーク](<b>断末魔:</b>3/2の武器1枚を自分の手札に追加する。)
#[LOE_012][墓荒らし](<b>断末魔:</b> 自分の手札に「コイン」1枚を追加する。)
#[LOE_019][掘り起こされたラプター]([x]<b>雄叫び:</b> 味方のミニオン1体を選択する。そのミニオンの____<b>断末魔</b>の能力をコピーする。)
#[LOE_046][巨大ガマ](<b>断末魔:</b> ランダムな敵1体に1ダメージを与える。)
#[LOE_061][アヌビサス・センチネル]([x]<b>断末魔:</b>ランダムな味方のミニオン1体に____+3/+3を付与する。)
#[LOE_089][ふらつくこびと達](<b>断末魔:</b> 2/2のこびとを3体召喚する。)
#[LOOT_144][護宝のドラゴン]([x]<b>断末魔:</b>相手に「コイン」2枚を与える。)
#[LOOT_153][ヴァイオレット・ヴルム](<b>断末魔:</b>1/1の「芋虫」を7体召喚する。)
#[LOOT_161][肉食キューブ]([x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。)
#[LOOT_184][シルバーヴァンガード]([x]<b>断末魔:</b>コスト8のミニオンを1体<b>招集</b>する。)
#[LOOT_233][呪われた門弟]([x]<b>断末魔:</b>5/1のレヴナントを1体召喚する。)
#[LOOT_412][コボルトの幻術師]([x]<b>断末魔:</b>自分の手札からミニオン1体の1/1のコピーを1体召喚する。)
#[LOOT_413][装甲虫](<b>断末魔:</b>装甲を3獲得する。)
#[LOOT_503][オニキスの小呪文石]([x]ランダムな敵のミニオン1体を破壊する。@<i>（<b>断末魔</b>カードを3枚手札から使用するとアップグレード）</i>)
#[LOOT_542][大逆の刃キングスベイン](付与された効果を常に維持する。<b>断末魔:</b>この武器を自分のデッキに混ぜる。)
#[OG_072][地の底の探索](<b>断末魔</b>を持つカード1枚を<b>発見</b>する。)
#[OG_080][蠱毒なザリル]([x]<b>雄叫び＆断末魔:</b> ランダムな毒素カード1枚を自分の手札に追加する。)
#[OG_133][頽廃させしものン＝ゾス](<b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。)
#[OG_147][狂闘品のヒールロボ]([x]<b>断末魔:</b>敵のヒーローの体力を#8回復する。)
#[OG_151][ン＝ゾスの触手](<b>断末魔:</b> 全てのミニオンに1ダメージを与える。)
#[OG_158][熱く教えを乞うもの](<b>断末魔:</b> ランダムな味方のミニオン1体に+1/+1を付与する。)
#[OG_249][蝕まれしトーレン]([x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。)
#[OG_256][ン＝ゾスの落とし子]([x]<b>断末魔:</b>味方のミニオン全てに+1/+1を付与する。)
#[OG_267][南海のスキッドフェイス]([x]<b>断末魔:</b> 自分の武器に___攻撃力+2を付与する。)
#[OG_272][黄昏の鎚の召喚師](<b>断末魔:</b> 5/5の無貌の破壊者を1体召喚する。)
#[OG_317][竜王デスウィング]([x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。)
#[OG_323][汚染利品グログロ君](<b>断末魔:</b> カードを1枚引く。)
#[OG_330][アンダーシティの押し売り]([x]<b>断末魔:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。)
#[SCH_162][ヴェクタス]([x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。)
#[SCH_426][潜入者リリアン]([x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。)
#[SCH_707][空を翔けるトビウオ]([x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。)
#[SCH_708][日陰草の非行生徒]([x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。)
#[SCH_709][イキってる四年生]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。)
#[SCH_711][疫病始祖ドレイク]([x]<b>断末魔:</b>ランダムなコスト7のミニオン1体を召喚する。)
#[SCH_714][英才エレク]([x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。)
#[TRL_074][ギザギザの歯]([x]<b>断末魔:</b>味方のミニオン全てに<b>急襲</b>を付与する。)
#[TRL_363][サロナイト鉱山の奴隷監督]([x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。)
#[TRL_409][サメのロア・グラル]([x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。)
#[TRL_503][スカラベの卵]([x]<b>断末魔:</b>1/1の「スカラベ」を3体召喚する。)
#[TRL_505][ひ弱なヒナ](<b>断末魔:</b>自分の手札の獣1体のコストを（1）減らす。)
#[TRL_520][マーロック・テイスティーフィン]([x]<b>断末魔:</b>自分のデッキから__マーロックを2体引く。)
#[TRL_525][闘技場の宝箱](<b>断末魔:</b>カードを2枚引く。)
#[TRL_531][ランブルタスク・シェイカー]([x]<b>断末魔:</b>3/2の「ランブルタスク・ブレイカー」を1体召喚する。)
#[TRL_537][ダ・アンダテイカ]([x]<b>雄叫び:</b>この対戦で死亡した味方のミニオン3体の_____<b>断末魔</b>を獲得する。_)
#[TRL_541][魂剥ぐロア・ハッカー]([x]<b>断末魔:</b>各プレイヤーのデッキに「ケガレた血」を1枚ずつ混ぜる。)
#[ULD_174][ヘビの卵](<b>断末魔:</b>3/4の「シーサーペント」を1体召喚する。)
#[ULD_177][オクトサリ](<b>断末魔:</b>カードを8枚引く。)
#[ULD_183][アヌビサス・ウォーブリンガー](<b>断末魔:</b>自分の手札のミニオン全てに+3/+3を付与する。)
#[ULD_184][コボルトのサンドトルーパー]([x]<b>断末魔:</b>敵のヒーローに___3ダメージを与える。)
#[ULD_208][カルトゥートの守護者]([x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。)
#[ULD_250][虫食いゴブリン]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。)
#[ULD_280][サーケットの昏倒強盗](<b>断末魔:</b>ランダムな敵のミニオン1体を___相手の手札に戻す。)
#[ULD_282][壺の商人]([x]<b>断末魔:</b>ランダムなコスト1のミニオン1体を____自分の手札に追加する。)
#[ULD_288][斂葬のアンカ]([x]<b>雄叫び:</b>自分の手札の<b>断末魔</b>を持つ各ミニオンをそれぞれコスト（1）の1/1に変える。)
#[ULD_706][バレバレの囮]([x]<b>断末魔:</b>各プレイヤーは手札の最もコストが低いミニオンを1体召喚する。)
#[UNG_010][満腹のスレッシャドン]([x]<b>断末魔:</b>1/1のマーロックを3体召喚する。)
#[UNG_065][死体花シェラジン]([x]<b>断末魔:</b><b>休眠状態</b>になる。1ターン中に4枚のカードを手札から使用すると______このミニオンは復活する。_)
#[UNG_076][卵泥棒]([x]<b>断末魔:</b>1/1のラプターを2体召喚する。)
#[UNG_083][デビルサウルスの卵]([x]<b>断末魔:</b>5/5のデビルサウルスを1体召喚する。)
#[UNG_818][即発のエレメンタル](<b>断末魔:</b>ランダムな敵のミニオン1体に　3ダメージを与える。)
#[UNG_845][火成のエレメンタル]([x]<b>断末魔:</b>1/2のエレメンタル2体を自分の手札に追加する。)
#[UNG_900][霊の歌い手ウンブラ](自分がミニオンを召喚した後そのミニオンの<b>断末魔</b>を発動する。)
#[YOD_016][飛掠船員](<b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。)

	elif '雄叫び' in dscrpt:#場に出たときに発動
		#基本的にいつでも。内容によっては場との関連がありうる。
		#内容の精査が必要
#[AT_115][フェンシングのコーチ](<b>雄叫び:</b> [x]次に自分のヒーローパワーを使う時、そのコストが（2）減る。)
#[AT_117][司会者](<b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。)
#[AT_118][グランド・クルセイダー](<b>雄叫び:</b> ランダムなパラディン用カード1枚を自分の手札に追加する。)
#[AT_121][花形選手](自分が<b>雄叫び</b>を持つカードを使う度+1/+1を獲得する。)
#[AT_122][串刺しのゴーモック](<b>雄叫び:</b> このミニオンを除いて味方に4体以上ミニオンがいる場合4ダメージを与える。)
#[AT_132][ジャスティサー・トゥルーハート]([x]<b>雄叫び:</b>自分のヒーローパワーが強化版に代わる。)
#[AT_133][ガジェッツァンの槍試合選手]([x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合__+1/+1を獲得する。)
#[BOT_079][忠実ロボ・ルミ]([x]<b>雄叫び:</b>味方のメカ1体に__+1/+1を付与する。)
#[BOT_083][毒物学者]([x]<b>雄叫び:</b>自分の武器に___攻撃力+1を付与する。)
#[BOT_243][マイラ・ロットスプリング]([x]<b>雄叫び:</b><b>断末魔</b>を持つミニオンを1体<b>発見</b>する。さらにそのミニオンの__<b>断末魔</b>を獲得する。)
#[BOT_270][含み笑う発明家]([x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。)
#[BOT_283][ホッピング・ホッパー]([x]<b>雄叫び:</b>この対戦で自分が手札から使用した他の「ホッピング・ホッパー」1体につき_+2/+2を獲得する。)
#[BOT_288][ラボの採用担当者]([x]<b>雄叫び:</b>味方のミニオン1体のコピー3枚を____自分のデッキに混ぜる。)
#[BOT_296][オメガ・ディフェンダー]([x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_)
#[BOT_308][スプリング・ロケット](<b>雄叫び:</b>2ダメージを与える。)
#[BOT_413][ブレインストーマー]([x]<b>雄叫び:</b>自分の手札の呪文1枚につき_____体力+1を獲得する。)
#[BOT_431][グルグルグライダー]([x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を1体召喚する。)
#[BOT_447][結晶術師]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_)
#[BOT_448][損傷したステゴトロン](<b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。)
#[BOT_511][シーフォーリウム・ボンバー]([x]<b>雄叫び:</b>相手のデッキに「爆弾」1枚を混ぜる。「爆弾」は引かれた際に爆発し__5ダメージを与える。)
#[BOT_532][エクスプローディネーター]([x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を___2体召喚する。)
#[BOT_535][マイクロロボ操縦者]([x]<b>雄叫び:</b>1/1の「マイクロロボ」を___2体召喚する。)
#[BOT_538][スパーク・エンジン]([x]<b>雄叫び:</b><b>急襲</b>を持つ1/1の「スパーク」1体を____自分の手札に追加する。)
#[BOT_539][魔力ダイナモ]([x]<b>雄叫び:</b>コスト（5）以上の呪文を1枚<b>発見</b>する。)
#[BOT_540][電磁パルス工作員]([x]<b>雄叫び:</b>__メカ1体を破壊する。)
#[BOT_544][逃走する試験体]([x]<b>雄叫び:</b>合計6ダメージを自身を除く味方のミニオンにランダムに振り分ける。)
#[BOT_550][電気職工]([x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__+1/+1を獲得する。)
#[BOT_552][天体配列者]([x]<b>雄叫び:</b>味方に体力7のミニオンが3体以上いる場合全ての敵に_7ダメージを与える。)
#[BOT_562][カッパーテイルモドキ]([x]<b>雄叫び:</b>次の自分のターンまで__<b>隠れ身</b>を獲得する。)
#[BOT_573][実験台9号](<b>雄叫び:</b>自分のデッキから異なる<b>秘策</b>を5枚引く。)
#[BOT_907][電設ロボ](<b>雄叫び:</b>自分の手札のメカ全てのコストを（1）減らす。)
#[BRM_008][ダークアイアン・スカルカー]([x]<b>雄叫び:</b>ダメージを受けていない敵のミニオン全てに____2ダメージを与える。)
#[BRM_024][ドラコニッド・クラッシャー]([x]<b>雄叫び:</b> 相手の体力が15以下の場合____+3/+3を獲得する。)
#[BRM_026][腹ペコのドラゴン](<b>雄叫び:</b> ランダムなコスト1のミニオン1体を相手の陣地に召喚する。)
#[BRM_029][レンド・ブラックハンド]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合<b>レジェンド</b>ミニオン1体を破壊する。)
#[BRM_030][ネファリアン]([x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムな呪文2枚を____自分の手札に追加する。)
#[BRM_033][ブラックウィングの技術者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合____+1/+1を獲得する。)
#[BRM_034][ブラックウィングの変性者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合_____3ダメージを与える。)
#[BT_010][フェルフィンのナビ](<b>雄叫び:</b>自身を除く味方のマーロックに___+1/+1を付与する。)
#[BT_126][テロン・ゴアフィーンド]([x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。)
#[BT_159][テラーガードの逃亡者](<b>雄叫び:</b>相手の陣地に1/1の「追手」を___3体召喚する。)
#[BT_160][錆鉄の狂信者]([x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。)
#[BT_702][アッシュタン・スレイヤー]([x]<b>雄叫び:</b><b>隠れ身</b>状態のミニオン1体にこのターンの間、攻撃力+3と<b>無敵</b>を付与する。)
#[BT_710][グレイハート族の賢者]([x]<b>雄叫び:</b>味方に<b>隠れ身</b>状態のミニオンがいる場合______カードを2枚引く。__)
#[BT_711][脳天直撃ガール]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合ミニオン1体を所有者の手札に戻す。そのコストは（1）増える。)
#[BT_714][冷たき影の紡ぎ手](<b>雄叫び:</b>敵1体を<b>凍結</b>させる。)
#[BT_717][穴掘りスコーピッド]([x]<b>雄叫び:</b>2ダメージを与える。これにより対象が死んだ場合<b>隠れ身</b>を獲得する。)
#[BT_720][錆鉄騎の略奪者](<b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。)
#[BT_722][ガーディアン改造屋]([x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>聖なる盾</b>を付与する。_)
#[BT_723][ロケット改造屋]([x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>急襲</b>を付与する。_)
#[BT_724][イセリアル改造屋]([x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。)
#[BT_729][荒野の看守]([x]<b>雄叫び:</b>ミニオン1体と、同種族の他のミニオン全てに__3ダメージを与える。)
#[BT_732][鋼拾いのシヴァーラ]([x]<b>雄叫び:</b>合計6ダメージを自身を除くミニオンに____ランダムに振り分ける。_)
#[BT_737][マイエヴ・シャドウソング]([x]<b>雄叫び:</b>ミニオン1体を選択する。そのミニオンは2ターンの間<b>休眠状態</b>になる。)
#[BT_850][マグゼリドン]([x]<b>休眠状態</b>。<b>雄叫び:</b>敵の陣地に1/3の結界師を3体召喚する。それらが死んだ時全てのミニオンを破壊して目覚める。)
		pass
	elif '秘策' in dscrpt:#固有の条件を満たすときに発動
		#基本的にいつでも。内容によっては場との関連がありうる。
#[BOT_573][実験台9号](<b>雄叫び:</b>自分のデッキから異なる<b>秘策</b>を5枚引く。)
#[BT_042][偽装](<b>秘策:</b>味方のミニオンが攻撃された時、それをコストが（3）高いランダムなミニオンに変身させる。)
#[BT_188][影宝石商ハナー]([x]自分が<b>秘策</b>を手札から使用した後別のクラスの_____<b>秘策</b>1つを<b>発見</b>する。)
#[BT_707][伏兵](<b>秘策:</b>相手がミニオンを手札から使用した後<b>猛毒</b>を持つ2/3の伏兵を1体召喚する。)
#[BT_709][汚い手]([x]<b>秘策:</b>相手が呪文を使用した後カードを2枚引く。)
#[BT_711][脳天直撃ガール]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合ミニオン1体を所有者の手札に戻す。そのコストは（1）増える。)
#[DAL_086][サンリーヴァーのスパイ]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合____+1/+1を獲得する。)
#[EX1_080][秘密の番人]([x]<b>秘策</b>が使用される度+1/+1を獲得する。)
#[EX1_186][SI:7潜入工作員]([x]<b>雄叫び:</b>ランダムな敵の___<b>秘策</b>1つを破壊する。)
#[FP1_004][マッドサイエンティスト]([x]<b>断末魔:</b> 自分のデッキにある_______<b>秘策</b>1枚を準備する。)
#[GIL_648][ギルニーアスの警部](<b>雄叫び:</b>敵の<b>秘策</b>全てを破壊する。)
#[GVG_074][ケザンのミスティック](<b>雄叫び:</b> 敵のランダムな<b>秘策</b>1つを自分のものにする。)
#[GVG_089][イルミネイター](自分のターンの終了時に<b>秘策</b>が準備されている場合自分のヒーローの体力を#4回復する。)
#[KAR_037][番鳥](<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。)
#[LOOT_204][九死一生](<b>秘策:</b>味方のミニオンが死亡した時、そのミニオン1体を自分の手札に戻す。そのコストは（2）減る。)
#[LOOT_210][突然の裏切り](<b>秘策:</b>ミニオンが自分のヒーローを攻撃した時、代わりにそのミニオンに隣接する誰かを攻撃する。)
#[LOOT_214][雲隠れ](<b>秘策:</b>自分のヒーローがダメージを受けた後このターンの間<b>無敵</b>になる。)
#[OG_254][秘密を喰らうもの]([x]<b>雄叫び:</b> 敵の<b>秘策</b>全てを破壊する。破壊した秘策1つにつき+1/+1を獲得する。)
#[SCH_706][カンニング]([x]<b>秘策:</b>相手のターンの終了時相手がそのターンに手札から使用した全てのカードのコピーを自分の手札に追加する。)
#[TRL_530][覆面選手]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合自分のデッキから___<b>秘策</b>を1つ準備する。)
		cond1 +=2
	elif '<b>挑発</b>' in dscrpt:
#[AT_017][トワイライトの守護者]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。)
#[AT_097][トーナメント参加者](<b>挑発</b>)
#[AT_112][槍試合の名手]([x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。)
#[AT_114][邪悪なる野次馬](<b>挑発</b>)
#[AT_123][チルモー]([x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。)
#[BOT_021][ブロンズ・ゲートキーパー](<b>超電磁</b><b>挑発</b>)
#[BOT_050][錆びついたリサイクラー](<b>挑発</b><b>生命奪取</b>)
#[BOT_270][含み笑う発明家]([x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。)
#[BOT_296][オメガ・ディフェンダー]([x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_)
#[BOT_448][損傷したステゴトロン](<b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。)
#[BOT_548][ジリアックス](<b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>)
#[BT_155][屑鉄山のコロッサス]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。)
#[BT_715][ボーンチューワーの喧嘩屋](<b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。)
#[BT_716][ボーンチューワーの前衛](<b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。)
#[BT_720][錆鉄騎の略奪者](<b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。)
#[BT_730][大物気取りのオーク](<b>挑発</b>体力が最大の場合このミニオンは____攻撃力+2を得る。)
#[CFM_652][二流の強面]([x]<b>挑発</b>相手の陣地に3体以上のミニオンがいる場合_____コストが（2）減る。)
#[CFM_653][日雇い護衛](<b>挑発</b>)
#[CFM_688][トゲ付きのホグライダー]([x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。)
#[CFM_790][ドブネズミ]([x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。)
#[CFM_806][ラシオン]([x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。)
#[CFM_854][満開の古代樹](<b>挑発</b>)
#[CS1_042][ゴールドシャイアの歩兵](<b>挑発</b>)
#[CS1_069][フェン・クリーパー](<b>挑発</b>)
#[CS2_121][フロストウルフの兵卒](<b>挑発</b>)
#[CS2_125][鉄毛のグリズリー](<b>挑発</b>)
#[CS2_127][シルバーバックの長](<b>挑発</b>)
#[CS2_162][闘技場の覇者](<b>挑発</b>)
#[CS2_179][センジン・シールドマスタ](<b>挑発</b>)
#[CS2_187][ブーティ・ベイのボディガード](<b>挑発</b>)
#[DAL_058][ヤジロボ](<b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。)
#[DAL_088][金庫番](<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。)
#[DAL_096][ヴァイオレット監獄の看守](<b>挑発</b><b>呪文ダメージ+1</b>)
#[DAL_551][誇り高き守護者]([x]<b>挑発</b>味方に他のミニオンがいない場合__攻撃力+2を得る。)
#[DAL_560][酒場のヒロイック女将]([x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_)
#[DAL_775][トンネル爆破係]([x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。)
#[DRG_064][ズルドラクの儀式官]([x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__)
#[DRG_065][ヒポグリフ](<b>急襲</b>、<b>挑発</b>)
#[DRG_242][ガラクロンドの盾](<b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。)
#[EX1_002][黒騎士]([x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。)
#[EX1_032][サンウォーカー]([x]<b>挑発</b>、<b>聖なる盾</b>)
#[EX1_058][サンフューリーの護衛]([x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。)
#[EX1_093][アルガスの守護者](<b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。)
#[EX1_097][涜れしもの]([x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。)
#[EX1_390][トーレン・ウォリアー]([x]<b>挑発</b>ダメージを受けている間は___攻撃力+3を得る。)
#[EX1_396][魔古山の番兵](<b>挑発</b>)
#[EX1_405][盾持ち](<b>挑発</b>)
#[FP1_012][ヘドロゲッパー]([x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。)
#[FP1_024][不安定なグール]([x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。)
#[GIL_120][怒れるエティン](<b>挑発</b>)
#[GIL_207][幽霊民兵](<b>木霊</b>、<b>挑発</b>)
#[GIL_526][ワームガード]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。)
#[GIL_527][フェルソウルの異端審問官](<b>生命奪取</b>、<b>挑発</b>)
#[GIL_623][ウィッチウッドのグリズリー]([x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。)
#[GIL_667][朽ちかけたアップルバウム]([x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。)
#[GIL_809][眠るスチームロボ](<b>挑発</b>)
#[GVG_085][マジウザ・オ・トロン](<b>挑発</b><b>聖なる盾</b>)
#[GVG_093][ターゲット・ダミー](<b>挑発</b>)
#[GVG_097][リトル・エクソシスト]([x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_)
#[GVG_098][ノームレガン歩兵]([x]<b>突撃</b>、<b>挑発</b>)
#[GVG_107][エンハンス・オ・メカーノ](<b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>)
#[ICC_314][リッチキング]([x]<b>挑発</b>自分のターンの終了時ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。)
#[ICC_466][サロナイト鉱山の奴隷]([x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。)
#[ICC_705][ボーンメア]([x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。)
#[ICC_853][ヴァラナール公爵]([x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。)
#[ICC_912][躯の駆り手]([x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。)
#[KAR_011][気取り屋の俳優](<b>挑発</b>)
#[KAR_037][番鳥](<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。)
#[KAR_061][キュレーター]([x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。)
#[KAR_710][魔力細工師](<b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。)
#[LOE_073][デビルサウルスの化石](<b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。)
#[LOOT_117][蝋のエレメンタル](<b>挑発</b><b>聖なる盾</b>)
#[LOOT_124][孤高の勇者]([x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。)
#[LOOT_131][グリーン・ジェリー]([x]自分のターンの終了時<b>挑発</b>を持つ1/2のウーズを1体召喚する。)
#[LOOT_137][眠れるドラゴン](<b>挑発</b>)
#[LOOT_315][トログのキノコ食い]([x]<b>挑発</b>、<b>猛毒</b>)
#[LOOT_383][飢えているエティン](<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。)
#[NEW1_022][悪辣なる海賊]([x]<b>挑発</b>自分の武器の攻撃力1につき_____コストが（1）減る。)
#[NEW1_040][ホガー]([x]自分のターンの終了時<b>挑発</b>を持つ2/2のノールを1体召喚する。)
#[OG_131][双皇帝ヴェク＝ロア]([x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。)
#[OG_145][マジヤバ・オ・トロン](<b>挑発</b>、<b>聖なる盾</b>)
#[OG_153][変・クリーパー](<b>挑発</b>)
#[OG_156][マーロックの鯛ド変態]([x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。)
#[OG_174][さまよう無貌のもの]([x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。)
#[OG_249][蝕まれしトーレン]([x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。)
#[OG_284][黄昏の鎚の地霊術師]([x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>)
#[OG_318][エルウィンの変災ホガー]([x]このミニオンがダメージを受ける度<b>挑発</b>を持つ2/2の　ノールを1体召喚する。)
#[OG_327][のたうつ触手](<b>挑発</b>)
#[OG_337][単眼の怪異]([x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。)
#[SCH_232][クリムゾンの竜学生]([x]<b>魔法活性:</b>攻撃力+1と<b>挑発</b>を獲得する。)
#[SCH_709][イキってる四年生]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。)
#[SCH_710][往餓術師]([x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。)
#[TRL_363][サロナイト鉱山の奴隷監督]([x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。)
#[TRL_513][モッシュオグの審判](<b>挑発</b>、<b>聖なる盾</b>)
#[TRL_514][大虎ノーム]([x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。)
#[TRL_515][会場警備係]([x]<b>挑発</b>敵のミニオン1体につきコストが（1）減る。)
#[TRL_524][シールドブレイカー](<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。)
#[TRL_550][アマニの戦熊](<b>急襲</b>、<b>挑発</b>)
#[ULD_178][シアマト]([x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。)
#[ULD_179][ファランクス指揮官]([x]味方の<b>挑発</b>を持つミニオン全ては攻撃力+2を得る。)
#[ULD_189][無貌の潜むもの]([x]<b>挑発</b>、<b>雄叫び:</b>このミニオンの体力を2倍にする。)
#[ULD_193][動くモニュメント](<b>挑発</b>)
#[ULD_198][うつろう蜃気楼]([x]<b>挑発</b>自分のターンの開始時このミニオンを____自分のデッキに混ぜる。)
#[ULD_208][カルトゥートの守護者]([x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。)
#[ULD_215][包帯ゴーレム]([x]<b>蘇り</b>自分のターンの終了時<b>挑発</b>を持つ1/1の「スカラベ」を1体召喚する。)
#[ULD_250][虫食いゴブリン]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。)
#[ULD_271][傷を負ったトルヴィア]([x]<b>挑発</b>、<b>雄叫び:</b>このミニオンに____3ダメージを与える。)
#[ULD_275][ボーン・レイス](<b>挑発</b>、<b>蘇り</b>)
#[UNG_070][トルヴィアのストーンシェイパー]([x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。)
#[UNG_071][巨大マストドン](<b>挑発</b>)
#[UNG_072][ストーンヒルの守護者]([x]<b>挑発</b>、<b>雄叫び:</b><b>挑発</b>を持つミニオン____1体を<b>発見</b>する。)
#[UNG_801][巣作りロック鳥]([x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。)
#[UNG_808][不屈のカタツムリ]([x]<b>挑発</b>、<b>猛毒</b>)
#[UNG_810][ステゴドン](<b>挑発</b>)
#[UNG_848][始祖ドレイク]([x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。)
#[UNG_907][オズラック]([x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。)
#[UNG_928][タール・クリーパー]([x]<b>挑発</b>相手のターン中は___攻撃力+2を得る。)
#[YOD_038][空賊大将クラッグ]([x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。)
		#このカードが挑発カードの場合
		#→味方の場に出ているカードが多いときはGO
		#挑発を付与するタイプの呪文の場合
		#→付与する対象のミニオンがある場合にはGO
		cond1 +=2
	if '聖なる盾' in dscrpt:#一回の攻撃を受けない
#[AT_087][アージェントの騎兵](<b>突撃:</b><b>聖なる盾</b>)
#[AT_095][静寂の騎士](<b>隠れ身</b><b>聖なる盾</b>)
#[AT_112][槍試合の名手]([x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。)
#[AT_129][フィヨラ・ライトベイン](<b>自分</b>がこのミニオンに対して呪文を使用する度<b>聖なる盾</b>を獲得する。)
#[BOT_270][含み笑う発明家]([x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。)
#[BOT_414][クロークスケイルの化学者](<b>隠れ身</b><b>聖なる盾</b>)
#[BOT_534][ブル・ドーザー](<b>聖なる盾</b>)
#[BOT_548][ジリアックス](<b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>)
#[BT_722][ガーディアン改造屋]([x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>聖なる盾</b>を付与する。_)
#[DAL_078][旅の治療師](<b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。)
#[DAL_085][ダララン・クルセイダー](<b>聖なる盾</b>)
#[DRG_079][躱し身のワーム](<b>聖なる盾</b>、<b>急襲</b>呪文とヒーローパワーの標的にならない。)
#[EX1_008][アージェントの従騎士](<b>聖なる盾</b>)
#[EX1_020][スカーレット・クルセイダー](<b>聖なる盾</b>)
#[EX1_023][シルバームーンの守護兵](<b>聖なる盾</b>)
#[EX1_032][サンウォーカー]([x]<b>挑発</b>、<b>聖なる盾</b>)
#[EX1_067][アージェントの司令官]([x]<b>突撃</b>、<b>聖なる盾</b>)
#[EX1_590][ブラッドナイト]([x]<b>雄叫び:</b> 全てのミニオンは<b>聖なる盾</b>を失う。失われた聖なる盾1つにつき+3/+3を獲得する。)
#[GIL_202][ギルニーアスの近衛兵]([x]<b>聖なる盾</b>、<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GVG_079][フォース・タンクMAX](<b>聖なる盾</b>)
#[GVG_085][マジウザ・オ・トロン](<b>挑発</b><b>聖なる盾</b>)
#[GVG_107][エンハンス・オ・メカーノ](<b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>)
#[ICC_912][躯の駆り手]([x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。)
#[ICC_913][穢れし狂信者](<b>聖なる盾</b><b>呪文ダメージ+1</b>)
#[LOOT_117][蝋のエレメンタル](<b>挑発</b><b>聖なる盾</b>)
#[LOOT_124][孤高の勇者]([x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。)
#[LOOT_125][石肌のバジリスク](<b>聖なる盾</b><b>猛毒</b>)
#[OG_145][マジヤバ・オ・トロン](<b>挑発</b>、<b>聖なる盾</b>)
#[OG_283][クトゥーンに選ばれし者]([x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>)
#[SCH_143][聖レイジャー](<b>聖なる盾</b>)
#[TRL_513][モッシュオグの審判](<b>挑発</b>、<b>聖なる盾</b>)
#[ULD_178][シアマト]([x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。)
#[ULD_721][月の巨像](<b>聖なる盾</b>、<b>蘇り</b>)
#[UNG_070][トルヴィアのストーンシェイパー]([x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。)
		pass
	if '隠れ身' in dscrpt:#こちらから攻撃するまでの攻撃対象にならない
#[AT_095][静寂の騎士](<b>隠れ身</b><b>聖なる盾</b>)
#[BOT_414][クロークスケイルの化学者](<b>隠れ身</b><b>聖なる盾</b>)
#[BOT_555][先遣者セレスティア]([x]<b>隠れ身</b>相手がミニオンを手札から使用した後そのミニオンの_コピーになる。)
#[BOT_562][カッパーテイルモドキ]([x]<b>雄叫び:</b>次の自分のターンまで__<b>隠れ身</b>を獲得する。)
#[BT_701][スパイミストレス](<b>隠れ身</b>)
#[BT_702][アッシュタン・スレイヤー]([x]<b>雄叫び:</b><b>隠れ身</b>状態のミニオン1体にこのターンの間、攻撃力+3と<b>無敵</b>を付与する。)
#[BT_703][呪われた流れ者]([x]<b>断末魔:</b><b>隠れ身</b>を持つ7/5の影を1体召喚する。)
#[BT_710][グレイハート族の賢者]([x]<b>雄叫び:</b>味方に<b>隠れ身</b>状態のミニオンがいる場合______カードを2枚引く。__)
#[BT_713][アカマ]([x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。)
#[BT_717][穴掘りスコーピッド]([x]<b>雄叫び:</b>2ダメージを与える。これにより対象が死んだ場合<b>隠れ身</b>を獲得する。)
#[CFM_344][飛刀手流忍者・六丸]([x]<b>隠れ身</b>このミニオンの攻撃でミニオンが 死亡した時、自分のデッキからマーロックを2体召喚する。)
#[CFM_634][蓮華凶手]([x]<b>隠れ身</b>このミニオンが攻撃してミニオンを倒す度に　<b>隠れ身</b>を獲得する。)
#[CFM_636][シャドウ・レイジャー](<b>隠れ身</b>)
#[CFM_656][裏街の探偵](<b>雄叫び:</b> 敵のミニオンは<b>隠れ身</b>を失う。)
#[CFM_691][翡翠の鎌刀]([x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_694][影の師匠]([x]<b>雄叫び:</b><b>隠れ身</b>を持つミニオン1体に　+2/+2を付与する。)
#[CFM_781][蒐集家シャク]([x]<b>隠れ身</b>このミニオンが攻撃する度相手のクラスのランダムなカード1枚を自分の手札に追加する。)
#[CS2_161][レイヴンホルトの暗殺者](<b>隠れ身</b>)
#[DAL_090][ヘンチ・クランの隠密](<b>隠れ身</b>)
#[DRG_074][擬装した飛行船]([x]<b>雄叫び:</b>次の自分のターンまで自身を除く味方のメカに<b>隠れ身</b>を付与する。)
#[EX1_010][ウォーゲンのスパイ](<b>隠れ身</b>)
#[EX1_017][ジャングル・パンサー](<b>隠れ身</b>)
#[EX1_028][ストラングルソーントラ](<b>隠れ身</b>)
#[EX1_128][隠蔽]([x]次の自分のターンまで味方のミニオン全てに<b>隠れ身</b>を付与する。)
#[EX1_522][埋伏の暗殺者]([x]<b>隠れ身</b>、<b>猛毒</b>)
#[FP1_005][ナクスラーマスの亡霊](<b>隠れ身:</b> 自分のターンの開始時+1/+1を獲得する。)
#[GVG_025][隻眼のチート]([x]自分が海賊を召喚する度、<b>隠れ身</b>を獲得する。)
#[GVG_081][ギルブリン・ストーカー](<b>隠れ身</b>)
#[GVG_088][オーガ・ニンジャ](<b>隠れ身:</b>50%の確率で、指定していない敵を攻撃する。)
#[GVG_109][ミニ・メイジ]([x]<b>呪文ダメージ+1</b><b>隠れ身</b>)
#[KAR_044][モローズ]([x]<b>隠れ身</b>自分のターンの終了時1/1の家令を1体召喚する。)
#[LOOT_136][潜む悪鬼](<b>隠れ身</b>自身を除く味方のミニオンは攻撃力+1を得る。)
#[NEW1_014][変装の達人](<b>雄叫び:</b> 次の自分のターンまで味方のミニオン1体に<b>隠れ身</b>を付与する。)
#[OG_247][ウォーゲン変異体](<b>隠れ身</b>)
#[SCH_234][偽善系の二年生]([x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。)
#[SCH_426][潜入者リリアン]([x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。)
#[SCH_708][日陰草の非行生徒]([x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。)
#[TRL_010][ハーフタイムの清掃員]([x]<b>隠れ身</b>、<b>血祭:</b>___装甲を3獲得する。)
#[TRL_092][サメの精霊]([x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。)
#[ULD_274][荒れ地の暗殺者](<b>隠れ身</b>、<b>蘇り</b>)
#[UNG_812][サーベルストーカー](<b>隠れ身</b>)
#[UNG_814][巨大スズメバチ]([x]<b>隠れ身</b>、<b>猛毒</b>)
#[YOD_006][脱走したマナセイバー]([x]<b>隠れ身</b>これが攻撃する度このターンの間のみマナクリスタルを1つ獲得する。)
#[YOD_016][飛掠船員](<b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。)
		pass
	elif '呪文ダメージ' in dscrpt:
		#攻撃呪文カードを持っていたら+2
#[AT_093][極寒のスノボルト](<b>呪文ダメージ+1</b>)
#[AT_117][司会者](<b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。)
#[BT_008][錆鉄の入門者]([x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。)
#[BT_724][イセリアル改造屋]([x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。)
#[CFM_039][路上のトリックスター](<b>呪文ダメージ+1</b>)
#[CS2_142][コボルトの地霊術師](<b>呪文ダメージ+1</b>)
#[CS2_155][大魔術師](<b>呪文ダメージ+1</b>)
#[CS2_197][オーガのメイジ達](<b>呪文ダメージ+1</b>)
#[DAL_089][呪文書綴じ師]([x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。)
#[DAL_096][ヴァイオレット監獄の看守](<b>挑発</b><b>呪文ダメージ+1</b>)
#[DAL_434][魔力の番人]([x]自分が<b>呪文ダメージ</b>を持っていない限り攻撃できない。)
#[DAL_548][アゼライト・エレメンタル]([x]自分のターンの開始時<b>呪文ダメージ+2</b>を得る。)
#[DAL_748][マナタンク](<b>呪文ダメージ+1</b>)
#[EX1_012][ブラッドメイジ・サルノス]([x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。)
#[EX1_284][アジュア・ドレイク]([x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。)
#[EX1_563][マリゴス](<b>呪文ダメージ+5</b>)
#[EX1_582][ダラランのメイジ](<b>呪文ダメージ+1</b>)
#[EX1_584][老練のメイジ]([x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。)
#[GIL_121][ダークマイア・ムーンキン](<b>呪文ダメージ+2</b>)
#[GIL_529][スペルシフター]([x]<b>呪文ダメージ+1</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GVG_109][ミニ・メイジ]([x]<b>呪文ダメージ+1</b><b>隠れ身</b>)
#[ICC_093][タスカーの漁師]([x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。)
#[ICC_856][スペルウィーヴァー](<b>呪文ダメージ+2</b>)
#[ICC_913][穢れし狂信者](<b>聖なる盾</b><b>呪文ダメージ+1</b>)
#[OG_082][コボルトの地霊呪痛死](<b>呪文ダメージ+2</b>)
#[SCH_245][筆記の執精]([x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。)
#[SCH_270][根源学の予習]([x]<b>呪文ダメージ</b>を持つミニオンを1体<b>発見</b>する。自分が次に使用する<b>呪文ダメージ</b>を持つミニオンのコストが（1）減る。)
#[SCH_273][ラス・フロストウィスパー]([x]自分のターンの終了時全ての敵に$1ダメージを与える<i>（<b>呪文ダメージ</b>によって__強化される）</i>。)
#[SCH_530][代理鏡師]([x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。)
#[TRL_312][強仙師](ダメージを受けている間は<b>呪文ダメージ+2</b>を得る。)
		pass
	elif '<b>沈黙</b>' in dscrpt:
		pass
#悪魔1体を<b>沈黙</b>させる->悪魔カードが相手の場に出ていたら
#<b>沈黙</b>させる->非バニラカードが相手の場に出ていたら
#<b>沈黙</b>させる->「攻撃できない」が自分の場に出ていたら
#[AT_106][光の勇者](<b>雄叫び:</b> 悪魔1体を<b>沈黙</b>させる。)
#[CFM_855][デファイアスの掃除屋]([x]<b>雄叫び:</b><b>断末魔</b>を持つミニオン1体を<b>沈黙</b>させる。)
#[CS2_203][鉄嘴のフクロウ]([x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。)
#[DAL_735][ダラランの司書](<b>雄叫び:</b>隣接するミニオンを<b>沈黙</b>させる。)
#[EX1_048][スペルブレイカー]([x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。)
#[FP1_016][泣き叫ぶ魂]([x]<b>雄叫び: </b>自身を除く味方のミニオンを_____<b>沈黙</b>させる。)
#[TRL_524][シールドブレイカー](<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。)
	elif '<b>猛毒</b>' in dscrpt:
#<b>猛毒</b>
		pass
	elif '<b>超電磁</b>' in dscrpt:
#<b>超電磁</b>
		pass
	elif '<b>急襲</b>' in dscrpt:
#<b>急襲</b>
		pass
	elif '<b>生命奪取</b>' in dscrpt:
#<b>生命奪取</b>
		pass
	elif '<b>休眠状態</b>' in dscrpt:
#<b>休眠状態</b>
		pass
	elif '<b>発見</b>' in dscrpt:
#<b>発見</b>
		pass

########### 度 #################

	elif '武器を装備する度' in dscrpt:
#[AT_029][バッカニーア](自分が武器を装備する度、その武器に攻撃力+1を付与する。)
#[CFM_325][ちんけなバッカニーア]([x]自分のヒーローが武器を装備している場合攻撃力+2を得る。)
#[GVG_119][ブリングトロン3000](<b>雄叫び:</b> 各プレイヤーはランダムな武器を装備する。)
		cond1 += 1
		for card in player.characters:
			if card.type == CardType.WEAPON:
				cond1 += 1
	elif 'ヒーローを攻撃する度' in dscrpt:
#[AT_032][闇商人]([x]<b>雄叫び:</b>味方に海賊がいる場合___+1/+1を獲得する。)
#[AT_070][空賊船長クラッグ](<b>突撃ィィィィ</b>味方の海賊1体につきコストが（1）減る。)
#[NEW1_027][南海の船長](自身を除く味方の海賊は+1/+1を得る。)
#[TRL_127][大砲連射]([x]ランダムな敵1体に$3ダメージを与える。味方の海賊1体につき1回これを繰り返す。)
		if target!=None and target.type == CardType.HERO:
			cond1 += 2
#自分のヒーローがダメージを受ける度
#ヒーローを攻撃する度
#武器を装備する度

#このミニオンに対して呪文を使用する度
#このミニオンがダメージを受ける度
#このミニオンが攻撃してミニオンを倒す度
#このミニオンが攻撃する度
#味方のミニオンが死ぬ度

#自分が呪文を使う度
#相手が呪文を使う度
#自分がカードを引く度
#このカードが自分の手札にある間
#<b>雄叫び</b>を持つカードを使う度
#<b>雄叫び</b>を持つミニオンを召喚する度
#自分がカードをデッキに混ぜる度

#[CFM_807][競売王ビアードオ]([x]自分が呪文を使用した後自分のヒーローパワーを再度使用可能にする。
#[CFM_808][鮫のゲンゾー]([x]このミニオンが攻撃する度両プレイヤーは手札が3枚になるまでカードを引く。
#[CFM_851][敏腕記者]([x]相手がカードを引く度+1/+1を獲得する。
#[DAL_592][石頭]([x]<b>急襲</b>このミニオンの攻撃でミニオンが死亡した後__再度攻撃できる。
#[DAL_719][タク・ノズウィスカー]([x]自分がカードを自分のデッキに混ぜる度そのコピー1枚を自分の手札に追加する。
#[DAL_749][神出鬼没の怪人]([x]<b>断末魔:</b>このミニオンの攻撃力が4以上の場合__再度召喚する。
#[DAL_771][金の猛者]([x]このミニオンが攻撃する度相手に「コイン」1枚を与える。
#[DAL_774][異境の乗騎売り]([x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。
#[DRG_036][ワクサドレッド]([x]<b>断末魔:</b>引かれた際「ワクサドレッド」を再度召喚するロウソク1枚を______自分のデッキに混ぜる。_
#[DRG_092][魔改造師]([x]自分がカードを引く度それをランダムな<b>レジェンド</b>ミニオンに変身させる。
#[EX1_001][ライトウォーデン]([x]キャラクターが回復を受ける度に攻撃力+2を獲得する。
#[EX1_007][苦痛の侍祭]([x]このミニオンがダメージを受ける度　カードを1枚引く。
#[EX1_044][クエスト中の冒険者]([x]自分がカードを使う度、+1/+1を獲得する。
#[EX1_055][マナ中毒者]([x]自分が呪文を使う度そのターンの間攻撃力+2を獲得する。
#[EX1_080][秘密の番人]([x]<b>秘策</b>が使用される度+1/+1を獲得する。
#[EX1_095][ガジェッツァンの競売人](自分が呪文を使う度カードを1枚引く。
#[EX1_100][探話士チョー](プレイヤーが呪文を使う度、もう1人のプレイヤーの手札にその呪文のコピーを追加する。
#[EX1_187][魔力喰らい]([x]自分が呪文を使う度+2/+2を獲得する。
#[EX1_399][グルバシの狂戦士](このミニオンがダメージを受ける度攻撃力+3を獲得する。
#[EX1_509][マーロックのタイドコーラー]([x]自分がマーロックを召喚する度___攻撃力+1を獲得する。
#[EX1_558][ハリソン・ジョーンズ](<b>雄叫び:</b> 敵の武器を破壊しその耐久度に等しい枚数のカードを引く。
#[FP1_028][墓掘り人]([x]自分が<b>断末魔</b>を持つミニオンを召喚する度__攻撃力+1を獲得する。
#[GIL_510][ミストレイス]([x]自分が<b>木霊</b>を持つカードを手札から使用する度____+1/+1を獲得する。
#[GIL_561][ブラックワルド・ピクシー]([x]<b>雄叫び:</b>自分のヒーローパワーを再度使用可能にする。
#[GIL_598][テス・グレイメイン]([x]<b>雄叫び:</b>この対戦で自分が手札から使用した他のクラスのカード全てを再度使用する<i>（対象はランダムに選択される）</i>。
#[GIL_620][人形師ドリアン]([x]自分がミニオンを引く度、そのミニオンの1/1のコピーを1体召喚する。
#[GIL_672][亡霊カトラス]([x]<b>生命奪取</b>自分が他のクラスのカードを手札から使用__する度、耐久度+1を獲得する。
#[GVG_016][フェル・リーヴァー](相手がカードを使う度自分のデッキの上から3枚のカードを捨てる。
#[GVG_025][隻眼のチート]([x]自分が海賊を召喚する度、<b>隠れ身</b>を獲得する。
#[GVG_028][商大公ガリーウィックス]([x]相手が呪文を使う度自分はその呪文のコピー1枚を獲得し、相手は「ガリーウィックスの______コイン」1枚を獲得する。_
#[GVG_067][ストーンスプリンター・トログ]([x]相手が呪文を使う度攻撃力+1を獲得する。
#[GVG_068][バーリー・ロックジョー・トログ]([x]相手が呪文を使う度攻撃力+2を獲得する。
#[GVG_104][ホブゴブリン]([x]自分が攻撃力1のミニオンを場に出す度そのミニオンに______+2/+2を付与する。
#[GVG_106][ジャンクロボ]([x]味方のメカが死ぬ度+2/+2を獲得する。
#[GVG_116][メカジニア・サーマプラッグ](敵のミニオンが死ぬ度に、レプラノームを1体召喚する。
#[GVG_117][ガズロウ]([x]自分がコスト1の呪文を使う度、ランダムなメカ1体を自分の手札に追加する。
#[GVG_118][アーシネイター・トログザー](相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。
#[ICC_031][ナイトハウラー](このミニオンがダメージを受ける度攻撃力+2を獲得する。
#[ICC_096][タタラボッチ](<b>雄叫び:</b>自分の手札の武器を全て破棄しそれらの攻撃力と耐久度を獲得する。
#[ICC_097][ダイダラ墓地]([x]自分の武器が破壊される度　+1/+1を獲得する。
#[ICC_201][骰は投げられた]([x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。
#[ICC_240][ルーン鍛冶場のヌシ]([x]自分のターン中自分の武器は耐久度を失わない。
#[ICC_257][死体蘇生者]([x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。
#[ICC_468][悲惨な農夫]([x]このミニオンが攻撃する度敵のヒーローに_____2ダメージを与える。
#[ICC_900][壊死のガイスト]([x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。
#[ICC_911][号泣のバンシー]([x]自分がカードを使う度自分のデッキの上から3枚のカードを除去する。
#[KAR_036][魔力異常体]([x]自分が呪文を使う度このミニオンに体力+1を付与する。
#[KAR_041][堀に潜むもの](<b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。
#[LOE_086][召喚石](自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。
#[LOOT_149][回廊漁り蟲]([x]このカードが手札にある間ミニオンが死ぬ度コストが（1）減る。
#[LOOT_541][キング・トグワグル]([x]<b>雄叫び:</b>相手とデッキを交換する。再度交換するための身代金の呪文1枚を相手に与える。
#[NEW1_025][ブラッドセイルの海賊]([x]<b>雄叫び:</b> 敵の武器の耐久度を1減らす。
#[NEW1_026][ヴァイオレット・アイの講師]([x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。
#[OG_318][エルウィンの変災ホガー]([x]このミニオンがダメージを受ける度<b>挑発</b>を持つ2/2の　ノールを1体召喚する。
#[OG_321][熱狂する信者]([x]<b>挑発:</b> __このミニオンがダメージを受ける度、自分のクトゥーンに+1/+1を付与する<i>（居場所は問わない）。</i>
#[SCH_259][智慧の宝珠]([x]自分のターンの開始時自分のデッキの一番上のカードを見る。耐久度を1失い、それをデッキの一番下に置くことができる。
#[SCH_425][ドクター・クラスティノフ]([x]<b>急襲</b>このミニオンが攻撃する度自分の武器に+1/+1を付与する。
#[SCH_710][往餓術師]([x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。
#[SCH_714][英才エレク]([x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
#[SCH_717][万鍵支配者アラバスター]([x]相手がカードを引く度そのコピー1枚を自分の手札に追加する。____そのコストは（1）。_
#[TRL_405][野生のビーストマスター]([x]自分が獣を引く度その獣に+2/+2を付与する。
#[TRL_535][オオアゴガメのシェルファイター]([x]隣接するミニオンがダメージを受ける度このミニオンが身代わりとなってそのダメージを受ける。
#[TRL_570][スープ売り]([x]自分のヒーローの体力を3以上回復する度カードを1枚引く。
#[tt_004][屍肉喰いのグール]([x]ミニオンが死ぬ度攻撃力+1を獲得する。
#[ULD_231][旋風脚流の達人]([x]自分が<b>コンボ</b>カードを手札から使用する度ランダムな<b>コンボ</b>カード1枚を自分の手札に追加する。
#[ULD_290][歴史愛好家]([x]自分がミニオンを手札から使用する度自分の手札のランダムなミニオン1体に+1/+1を付与する。
#[UNG_087][ビタータイド・ヒドラ](このミニオンがダメージを受ける度自分のヒーローに___3ダメージを与える。
#[YOD_006][脱走したマナセイバー]([x]<b>隠れ身</b>これが攻撃する度このターンの間のみマナクリスタルを1つ獲得する。


############# 場合 #########################

	elif '自分の手札にドラゴンがいる場合' in dscrpt:
#[AT_017][トワイライトの守護者]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。)
#[AT_123][チルモー]([x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。)
#[BOT_066][メカ・チビドラゴン]([x]<b>断末魔:</b>7/7の「メカ・ドラゴン」を__1体召喚する。)
#[BRM_022][ドラゴンの卵](このミニオンがダメージを受ける度2/1のチビドラゴン1体を召喚する。)
#[BRM_029][レンド・ブラックハンド]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合<b>レジェンド</b>ミニオン1体を破壊する。)
#[BRM_033][ブラックウィングの技術者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合____+1/+1を獲得する。)
#[BRM_034][ブラックウィングの変性者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合_____3ダメージを与える。)
#[BT_726][ドラゴンモーの飛行追跡者](<b>断末魔:</b>3/4の「ドラゴンライダー」を1体召喚する。)
#[CFM_806][ラシオン]([x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。)
#[DRG_033][蝋竜の息吹]([x]__カードを3枚引く。自分の手札にドラゴンがいる間コストが（3）減る。)
#[DRG_049][美味しいマロバルーン](<b>断末魔:</b>自分の手札のドラゴン1体に__+2/+2を付与する。)
#[DRG_058][ウィングコマンダー]([x]自分の手札のドラゴン1体につき__攻撃力+2を得る。)
#[DRG_063][ドラゴンモーの密猟者](<b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。)
#[DRG_070][ドラゴンブリーダー](<b>雄叫び:</b>味方のドラゴン1体を選択する。そのコピー1体を自分の手札に追加する。)
#[DRG_072][スカイフィン](<b>雄叫び:</b>自分の手札にドラゴンがいる場合ランダムなマーロックを2体召喚する。)
#[DRG_077][ウトガルドのグラップル狙撃手]([x]<b>雄叫び:</b>両プレイヤーはカードを1枚引く。それがドラゴンだった場合召喚する。)
#[DRG_081][スケイルライダー]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____2ダメージを与える。)
#[DRG_086][クロマティックの卵]([x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！)
#[DRG_089][竜の女王アレクストラーザ]([x]<b>雄叫び:</b>_自分のデッキに重複するカードがない場合自身を除くランダムなドラゴン2体を自分の手札に追加する。____それらのコストは（1）になる。)
#[DRG_257][フリズ・キンドルルースト](<b>雄叫び:</b>自分のデッキのドラゴン全てのコストを（2）減らす。)
#[EX1_025][ミニドラゴン・メカニック]([x]<b>雄叫び:</b> 2/1のメカ・ミニドラゴンを[b]1体召喚する。)
#[EX1_116][リロイ・ジェンキンス]([x]<b>突撃</b>、<b>雄叫び:</b> 敵の陣地に1/1のチビドラゴンを2体召喚する。)
#[EX1_562][オニクシア]([x]<b>雄叫び:</b>自分の陣地が満員になる数の1/1のチビドラゴンを召喚する。)
#[GIL_526][ワームガード]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。)
#[GIL_601][スケイルワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。)
#[GIL_681][悪夢の融合体]([x]<i>これはエレメンタル、メカ、悪魔、マーロック、ドラゴン、獣、海賊、トーテムである。</i>)
#[GIL_816][沼のドラゴンの卵]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[ICC_027][ボーン・ドレイク]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[KAR_033][ブック・ワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力3以下の敵の______ミニオン1体を破壊する。_)
#[KAR_061][キュレーター]([x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。)
#[KAR_062][ネザースパイトの歴史家]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合____ドラゴン1体を<b>発見</b>する。)
#[KAR_095][動物園ロボ]([x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+1/+1を付与する。)
#[KAR_702][動物園の奇術師]([x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+2/+2を付与する。)
#[LOOT_132][ドラゴンスレイヤー](<b>雄叫び:</b>ドラゴン1体に6ダメージを与える。)
#[LOOT_540][ドラゴン孵化師]([x]自分のターンの終了時ドラゴンを1体<b>招集</b>する。)
#スレッド 'MainThread' (0x1) はコード 0 (0x0) で終了しました。
#[OG_317][竜王デスウィング]([x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。)
#[SCH_162][ヴェクタス]([x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。)
#[TRL_523][ファイアーツリーの呪術医]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____呪文を1つ<b>発見</b>する。)
#[TRL_569][ドッカンドラゴン](<b>雄叫び:</b>自分の手札にドラゴンがいる場合敵のミニオン1体に__7ダメージを与える。)
		for card in player.hand:
			if card.race == Race.DRAGON:
				cond1 += 2

############### キーワード #####################	
	elif 'コンボ' in dscrpt:
#[AT_028][シャドーパン騎兵](<b>コンボ:</b> 攻撃力+3を獲得する。)
#[AT_030][アンダーシティの勇士](<b>コンボ:</b> 1ダメージを与える。)
#[BOT_576][イカレた化学者]([x]<b>コンボ:</b>味方のミニオン1体に__攻撃力+4を付与する。)
#[CFM_690][翡翠の手裏剣]([x]__$2ダメージを与える。<b>コンボ:</b> {0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]__$2ダメージを与える。<b>コンボ:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_693][ガジェッツァンの渡し守]([x]<b>コンボ:</b>味方のミニオン1体を___自分の手札に戻す。)
#[CS2_073][冷血]([x]ミニオン1体に攻撃力+2を付与する。<b>コンボ:</b> 代わりに攻撃力+4を付与する。)
#[DAL_415][悪党同盟の悪漢]([x]<b>コンボ:</b>ランダムな<b>悪の手先</b>2体を自分の手札に追加する。)
#[DRG_031][ネクリウムの薬師]([x]<b>コンボ:</b>自分のデッキから<b>断末魔</b>を持つミニオンを1体引きその<b>断末魔</b>を獲得する。)
#[EX1_124][腹裂き]([x]$2ダメージを与える。<b>コンボ:</b> 代わりに$4ダメージを与える。)
#[EX1_131][デファイアスの親方]([x]<b>コンボ:</b>2/1のデファイアスの盗賊を1体召喚する。)
#[EX1_133][地獄送りの刃]([x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。)
#[EX1_134][SI:7諜報員]([x]<b>コンボ:</b> 2ダメージを与える。)
#[EX1_137][脳天直撃]([x]敵のヒーローに$2ダメージを与える。<b>コンボ:</b> 次のターン、このカードを自分の手札に戻す。)
#[EX1_613][エドウィン・ヴァンクリーフ](<b>コンボ:</b>このターン中で先に使用されたカード1枚につき+2/+2を獲得する。)
#[GIL_557][呪われた漂流者]([x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。)
#[GIL_902][人斬りバッカニーア](<b>コンボ:</b>自分の武器に攻撃力+1を__付与する。)
#[GVG_022][ティンカーの刃研ぎ油](自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。)
#[GVG_047][サボタージュ]([x]ランダムな敵のミニオン1体を破壊する。<b>コンボ:</b> さらに敵の武器を破壊する。)
#[ICC_809][疫病科学者]([x]<b>コンボ:</b>味方のミニオン1体に<b>猛毒</b>を付与する。)
#[ICC_910][略奪の亡霊]([x]<b>コンボ:</b>このターン中で先に使用したカードの枚数に等しいダメージを与える。)
#[LOOT_211][エルフの吟遊楽人]([x]<b>コンボ:</b>自分のデッキから__ミニオンを2体引く。)
#[NEW1_005][誘拐魔]([x]<b>コンボ:</b> ミニオン1体を___所有者の手札に戻す。)
#[OG_070][凶刃の狂信者]([x]<b>コンボ:</b>______+1/+1を獲得する。)
#[SCH_234][偽善系の二年生]([x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。)
#[SCH_350][ワンド泥棒]([x]<b>コンボ:</b>メイジの呪文を1つ<b>発見</b>する。)
#[SCH_509][頭を冷やせ！]([x]ミニオン1体を<b>凍結</b>させる。<b>コンボ:</b>さらに$3ダメージを与える。)
#[SCH_521][無理強い]([x]ダメージを受けているミニオン1体を破壊する。<b>コンボ:</b>ミニオン1体を破壊する。)
#[TRL_092][サメの精霊]([x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。)
#[TRL_124][ぶんどり部隊](自分のデッキから海賊を2体引く。<b>コンボ:</b>さらに武器を1つ引く。)
#[ULD_231][旋風脚流の達人]([x]自分が<b>コンボ</b>カードを手札から使用する度ランダムな<b>コンボ</b>カード1枚を自分の手札に追加する。)
#スレッド 'MainThread' (0x1) はコード 0 (0x0) で終了しました。
#[ULD_285][鉤付きシミター](<b>コンボ:</b>攻撃力+2を獲得する。)
#[UNG_063][カミツキソウ](<b>コンボ:</b> このターン中で先に使用されたカード1枚につき+1/+1を獲得する。)
#[UNG_064][ヴァイルスパイン・スレイヤー](<b>コンボ:</b>ミニオン1体を破壊する。)
#[YOD_017][影の彫刻家]([x]<b>コンボ:</b>このターン中に先に使用されたカード1枚につきカードを1枚引く。)
		if player.combo:
			cond1 += 2
	elif '味方に海賊がいる' in dscrpt or '味方の海賊' in dscrpt:
#[AT_032][闇商人]([x]<b>雄叫び:</b>味方に海賊がいる場合___+1/+1を獲得する。)
#[AT_070][空賊船長クラッグ](<b>突撃ィィィィ</b>味方の海賊1体につきコストが（1）減る。)
#[NEW1_027][南海の船長](自身を除く味方の海賊は+1/+1を得る。)
#[TRL_071][ブラッドセイルの吠猿]([x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方の海賊1体につき+1/+1を獲得する。)
#[TRL_127][大砲連射]([x]ランダムな敵1体に$3ダメージを与える。味方の海賊1体につき1回これを繰り返す。)
		for card in player.characters:
			if card.race == Race.PIRATE:
				cond1 += 2

#使わない
#[BOT_447][結晶術師]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_)
#[TRL_546][凶暴なリクガメ]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。)
#[UNG_087][ビタータイド・ヒドラ](このミニオンがダメージを受ける度自分のヒーローに___3ダメージを与える。)






#味方のミニオンが攻撃された時、and 変身させる
#自分のターンの終了時
#このターンに自分が呪文を使用した___場合
#味方に体力6以上のミニオンがいる場合
#自分の武器の攻撃力が3以上ある場合
#このミニオンの攻撃でミニオンが 死亡した時
#自分のデッキに重複するカードがない場合
#このターンの間のみ
#相手の陣地に3体以上のミニオンがいる場合
#自分のターンの終了時



#コストは（1）になる。
#を1体召喚する
#を2体召喚する
#を3体召喚する
#自分のデッキの残りのカードを__全て引く。
#攻撃力+4を付与する
#カードを1枚引く
#敵のミニオン1体に__4ダメージを与える
#自分の_____手札に追加する
#自分のデッキに混ぜる
#これのコピーに変身させる
#自分のデッキに混ぜる

#[CFM_655][有毒下水ウーズ]([x]<b>雄叫び:</b>敵の武器の耐久度を1減らす。)
#[CFM_656][裏街の探偵](<b>雄叫び:</b> 敵のミニオンは<b>隠れ身</b>を失う。)
#[CFM_658][奥部屋の用心棒]([x]味方のミニオンが死ぬ度、攻撃力+1を獲得する。)
#[CFM_659][ガジェッツァンのセレブ](<b>雄叫び:</b>体力を#2回復する。)
#[CFM_665][ウォーゲンのツッパリ]()
#[CFM_666][グルックフーの達人](<b>疾風</b>)
#[CFM_667][爆弾部隊]([x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。)
#[CFM_668][ドッペルギャングスター]([x]<b>雄叫び:</b>このミニオンのコピーを2体召喚する。)
#[CFM_669][強盗ログ]([x]相手が呪文を使う度自分の手札に「コイン」1枚を追加する。)
#[CFM_670][ノッゲンフォッガー市長]([x]あらゆる行動の対象は　ランダムに選択される。)
#[CFM_672][マダム・ゴヤ]([x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンを自分のデッキのミニオン1体と入れ替える。)
#[CFM_685][ドン・ハン＝チョー](<b>雄叫び:</b>自分の手札のランダムなミニオン1体に+5/+5を付与する。)
#[CFM_688][トゲ付きのホグライダー]([x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。)
#[CFM_690][翡翠の手裏剣]([x]__$2ダメージを与える。<b>コンボ:</b> {0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]__$2ダメージを与える。<b>コンボ:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_691][翡翠の鎌刀]([x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_693][ガジェッツァンの渡し守]([x]<b>コンボ:</b>味方のミニオン1体を___自分の手札に戻す。)
#[CFM_694][影の師匠]([x]<b>雄叫び:</b><b>隠れ身</b>を持つミニオン1体に　+2/+2を付与する。)
#[CFM_715][翡翠の精霊]([x]<b>雄叫び:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_781][蒐集家シャク]([x]<b>隠れ身</b>このミニオンが攻撃する度相手のクラスのランダムなカード1枚を自分の手札に追加する。)
#[CFM_790][ドブネズミ]([x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。)
#[CFM_806][ラシオン]([x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。)
#[CFM_807][競売王ビアードオ]([x]自分が呪文を使用した後自分のヒーローパワーを再度使用可能にする。)
#[CFM_808][鮫のゲンゾー]([x]このミニオンが攻撃する度両プレイヤーは手札が3枚になるまでカードを引く。)
#[CFM_809][タナリスのホグチョッパー]([x]<b>雄叫び:</b>相手が手札を1枚も持っていない場合<b>突撃</b>を獲得する。)
#[CFM_810][ピチピチレザーのホグリーダー]([x]<b>雄叫び:</b>相手の手札が6枚以上ある場合_____<b>突撃</b>を獲得する。)
#[CFM_851][敏腕記者]([x]相手がカードを引く度+1/+1を獲得する。)
#[CFM_852][蓮華密使]([x]<b>雄叫び:</b>ドルイド、ローグまたはシャーマンの_____カードを1枚<b>発見</b>する。)
#[CFM_853][グライムストリートの運び屋](<b>雄叫び:</b>自分の手札のランダムなミニオン1体に+1/+1を付与する。)
#[CFM_854][満開の古代樹](<b>挑発</b>)
#[CFM_855][デファイアスの掃除屋]([x]<b>雄叫び:</b><b>断末魔</b>を持つミニオン1体を<b>沈黙</b>させる。)
#[CFM_902][アヤ・ブラックポー]([x]<b>雄叫び＆断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び＆断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CS1_042][ゴールドシャイアの歩兵](<b>挑発</b>)
#[CS1_069][フェン・クリーパー](<b>挑発</b>)
#[CS2_072][死角からの一刺し]([x]ダメージを受けていない[b]ミニオン1体に[b]$2ダメージを与える。)
#[CS2_073][冷血]([x]ミニオン1体に攻撃力+2を付与する。<b>コンボ:</b> 代わりに攻撃力+4を付与する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[CS2_074][致死毒](自分の武器に攻撃力+2を付与する。)
#[CS2_075][凶悪なる一撃]([x]敵のヒーローに$3ダメージを与える。)
#[CS2_076][暗殺](敵のミニオン1体を破壊する。)
#[CS2_077][逃げ足](カードを4枚引く。)
#[CS2_080][アサシンブレード]()
#[CS2_117][大地の円環の遠見師](<b>雄叫び:</b>体力を#3回復する。)
#[CS2_118][マグマ・レイジャー]()
#[CS2_119][オアシス・オオアゴガメ]()
#[CS2_120][リバー・クロコリスク]()
#[CS2_121][フロストウルフの兵卒](<b>挑発</b>)
#[CS2_122][レイドリーダー](自身を除く味方のミニオンは攻撃力+1を得る。)
#[CS2_124][ウルフライダー](<b>突撃</b>)
#[CS2_125][鉄毛のグリズリー](<b>挑発</b>)
#[CS2_127][シルバーバックの長](<b>挑発</b>)
#[CS2_131][ストームウィンドの騎士](<b>突撃</b>)
#[CS2_141][アイアンフォージのライフル兵](<b>雄叫び:</b> 1ダメージを与える。)
#[CS2_142][コボルトの地霊術師](<b>呪文ダメージ+1</b>)
#[CS2_146][南海の甲板員]([x]自分のヒーローが武器を装備している場合<b>突撃</b>を持つ。)
#[CS2_147][ノームの発明家](<b>雄叫び:</b> カードを1枚引く。)
#[CS2_150][ストームパイクのコマンドー](<b>雄叫び:</b> 2ダメージを与える。)
#[CS2_151][シルバーハンド騎士]([x]<b>雄叫び:</b>2/2の従騎士を1体召喚する。)
#[CS2_155][大魔術師](<b>呪文ダメージ+1</b>)
#[CS2_161][レイヴンホルトの暗殺者](<b>隠れ身</b>)
#[CS2_162][闘技場の覇者](<b>挑発</b>)
#[CS2_168][マーロックの襲撃兵]()
#[CS2_169][巣立ちのドラゴンホーク](<b>疾風</b>)
#[CS2_171][石牙のイノシシ](<b>突撃</b>)
#[CS2_172][ブラッドフェン・ラプター]()
#[CS2_173][ブルーギル・ウォリアー](<b>突撃</b>)
#[CS2_179][センジン・シールドマスタ](<b>挑発</b>)
#[CS2_181][傷を負った剣匠](<b>雄叫び:</b> 自身に4ダメージを与える。)
#[CS2_182][チルウィンドのイェティ]()
#[CS2_186][戦のゴーレム]()
#[CS2_187][ブーティ・ベイのボディガード](<b>挑発</b>)
#[CS2_188][鬼軍曹]([x]<b>雄叫び:</b>このターンの間ミニオン1体に______攻撃力+2を付与する。_)
#[CS2_189][エルフの射手](<b>雄叫び:</b> 1ダメージを与える。)
#[CS2_196][レイザーフェン・ハンター]([x]<b>雄叫び:</b> 1/1のイノシシを1体召喚する。)
#[CS2_197][オーガのメイジ達](<b>呪文ダメージ+1</b>)
#[CS2_200][ボルダーフィストのオーガ]()
#[CS2_201][コアハウンド]()
#[CS2_203][鉄嘴のフクロウ]([x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。)
#[CS2_213][無謀なロケット乗り](<b>突撃</b>)
#[CS2_221][性悪な鍛冶屋](このミニオンがダメージを受けている間、自分の武器は攻撃力+2を得る。)
#[CS2_222][ストームウィンドの勇者](自身を除く味方のミニオンは+1/+1を得る。)
#[CS2_226][フロストウルフの将軍]([x]<b>雄叫び:</b> 戦場にいる味方のミニオン1体につき____+1/+1を獲得する。)
#[CS2_227][ベンチャー社の傭兵]([x]自分のミニオン全てのコストが（3）増える。)
#[CS2_231][ウィスプ]()
#[CS2_233][千刃乱舞](自分の武器を破壊しその攻撃力に等しいダメージを敵のミニオン全てに与える。)
#[DAL_010][トグワグルの計略]([x]ミニオン1体を選択する。そのコピー@体を自分のデッキに混ぜる。<i>（毎ターン___アップグレード！）</i>)
#[DAL_058][ヤジロボ](<b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。)
#[DAL_077][毒々フィン]([x]<b>雄叫び:</b>味方のマーロック1体に<b>猛毒</b>を付与する。)
#[DAL_078][旅の治療師](<b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。)
#[DAL_081][魔除けの宝石職人]([x]<b>雄叫び:</b>次の自分のターンまで自分のヒーローは呪文とヒーローパワーの標的にならない。)
#[DAL_085][ダララン・クルセイダー](<b>聖なる盾</b>)
#[DAL_086][サンリーヴァーのスパイ]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合____+1/+1を獲得する。)
#[DAL_087][ヘンチ・クランの妖婆]([x]<b>雄叫び:</b>種族が「全て」である1/1の「融合体」を2体召喚する。)
#[DAL_088][金庫番](<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。)
#[DAL_089][呪文書綴じ師]([x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。)
#[DAL_090][ヘンチ・クランの隠密](<b>隠れ身</b>)
#[DAL_092][魔力の下僕]()
#[DAL_095][ヴァイオレット監獄の魔剣士]([x]<b>雄叫び:</b>自分の手札の呪文1枚につき____攻撃力+1を獲得する。)
#[DAL_096][ヴァイオレット監獄の看守](<b>挑発</b><b>呪文ダメージ+1</b>)
#[DAL_366][未確認の契約書]([x]ミニオン1体を破壊する。手札になった時ボーナス効果を1つ獲得する。)
#[DAL_400][悪党同盟の電線ネズミ]([x]<b>雄叫び:</b><b>悪の手先</b>1体を自分の手札に追加する。)
#[DAL_415][悪党同盟の悪漢]([x]<b>コンボ:</b>ランダムな<b>悪の手先</b>2体を自分の手札に追加する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[DAL_416][ヘンチ・クランの強盗]([x]<b>雄叫び:</b>他のクラスの呪文を1つ<b>発見</b>する。)
#[DAL_417][強盗王トグワグル]([x]<b>雄叫び:</b>味方に<b>悪の手先</b>がいる場合、素敵な_____宝物を1つ選択する。)
#[DAL_434][魔力の番人]([x]自分が<b>呪文ダメージ</b>を持っていない限り攻撃できない。)
#[DAL_538][こっそり妨害工作員]([x]<b>雄叫び:</b>相手は手札のランダムな呪文を1つ使用する。__<i>（対象はランダムに選択）</i>)
#[DAL_539][サンリーヴァーの戦魔術師]([x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__4ダメージを与える。)
#[DAL_544][ポーション売り]([x]<b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。)
#[DAL_546][バリスタのリンチェン]([x]<b>雄叫び:</b>自身を除く味方の<b>雄叫び</b>を持つミニオン全てのコピーを1枚ずつ______自分の手札に追加する。_)
#[DAL_548][アゼライト・エレメンタル]([x]自分のターンの開始時<b>呪文ダメージ+2</b>を得る。)
#[DAL_550][最下層ウーズ]([x]このミニオンがダメージを受けて生き延びた後このミニオンのコピーを1体召喚する。)
#[DAL_551][誇り高き守護者]([x]<b>挑発</b>味方に他のミニオンがいない場合__攻撃力+2を得る。)
#[DAL_553][悪い大噛み魔術師]([x]自分のターンの終了時ランダムなコスト6のミニオン1体を召喚する。)
#[DAL_554][シェフ・ノミ]([x]<b>雄叫び:</b>自分のデッキが空の場合6/6の「油火災のエレメンタル」を6体召喚する。)
#[DAL_558][大魔術師ヴァルゴス]([x]自分のターンの終了時自分がこのターンに使用した呪文1つを再使用する。<i>（対象はランダム）</i>)
#[DAL_560][酒場のヒロイック女将]([x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_)
#[DAL_565][ポータル・オーバーフィーンド](<b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。)
#[DAL_566][奇抜な書記官]([x]<b>断末魔:</b>1/1の「息巻く巻物」を4体召喚する。)
#[DAL_582][ポータルの番人](<b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。)
#[DAL_592][石頭]([x]<b>急襲</b>このミニオンの攻撃でミニオンが死亡した後__再度攻撃できる。)
#[DAL_714][最下層の故買屋]([x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合+1/+1と<b>急襲</b>を獲得する。)
#[DAL_716][血の復讐]([x]ミニオン1体に$4ダメージを与える。自分の手札に他のクラスのカードがある場合コスト（0）。)
#[DAL_719][タク・ノズウィスカー]([x]自分がカードを自分のデッキに混ぜる度そのコピー1枚を自分の手札に追加する。)
#[DAL_720][ワグル・ピック]([x]<b>断末魔:</b>ランダムな味方のミニオン1体を自分の手札に戻す。そのミニオンのコストは（2）減る。)
#[DAL_728][大脱出]([x]味方のミニオン全てを自分の_手札に戻す。)
#[DAL_735][ダラランの司書](<b>雄叫び:</b>隣接するミニオンを<b>沈黙</b>させる。)
#[DAL_736][文書管理官エリシアーナ]([x]<b>雄叫び:</b>カードを5枚<b>発見</b>する。そのコピー2枚ずつを自分のデッキと置き換える。)
#[DAL_742][渦巻く狂風]([x]<b>疾風</b>を持つ味方のミニオンは全て<b>メガ疾風</b>を得る。)
#[DAL_743][ヘンチ・クランの騎豚]([x]<b>急襲</b>、<b>断末魔:</b>1/1のマーロックを1体召喚する。)
#[DAL_744][無貌レイジャー]([x]<b>雄叫び:</b>味方のミニオン1体の___体力をコピーする。)
#[DAL_747][フライトマスター]([x]<b>雄叫び:</b>各プレイヤーの陣地に2/2の「グリフォン」を1体ずつ召喚する。)
#[DAL_748][マナタンク](<b>呪文ダメージ+1</b>)
#[DAL_749][神出鬼没の怪人]([x]<b>断末魔:</b>このミニオンの攻撃力が4以上の場合__再度召喚する。)
#[DAL_751][狂気の召喚師]([x]<b>雄叫び:</b>各プレイヤーの陣地に1/1の「インプ」を____可能な限り召喚する。)
#[DAL_752][ジェペット・ジョイバズ]([x]<b>雄叫び:</b>自分のデッキからミニオンを2体引く。それらの攻撃力、体力、コストを1に変える。)
#[DAL_760][バーリー・ショベルフィスト](<b>急襲</b>)
#[DAL_771][金の猛者]([x]このミニオンが攻撃する度相手に「コイン」1枚を与える。)
#[DAL_773][魔法の絨毯]([x]自分がコスト1のミニオンを手札から使用した後そのミニオンに攻撃力+1と<b>急襲</b>を付与する。)
#[DAL_774][異境の乗騎売り]([x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。)
#[DAL_775][トンネル爆破係]([x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。)
#[DAL_800][影マント・ザイル]([x]ザイルの悪党デッキの1つを使って対戦を開始する！)
#[DRG_027][陰の殺し屋]([x]<b>雄叫び:</b>既に2回<b>祈願</b>していた場合「コイン」3枚を____自分の手札に追加する。)
#[DRG_028][ドラゴンの宝の山]([x]他のクラスの<b>レジェンド</b>ミニオン1体を<b>発見</b>する。)
#[DRG_030][ガラクロンドを讃えよ！]([x]ミニオン1体に攻撃力+1を付与する。ガラクロンドに<b>祈願</b>する。)
#[DRG_031][ネクリウムの薬師]([x]<b>コンボ:</b>自分のデッキから<b>断末魔</b>を持つミニオンを1体引きその<b>断末魔</b>を獲得する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[DRG_033][蝋竜の息吹]([x]__カードを3枚引く。自分の手札にドラゴンがいる間コストが（3）減る。)
#[DRG_034][密航者]([x]<b>雄叫び:</b>自分のデッキに対戦開始時になかったカードがある場合、それらを2枚まで引く。)
#[DRG_035][ブラッドセイルのスカイ賊]([x]<b>雄叫び:</b>1/1の海賊2体を__自分の手札に追加する。)
#[DRG_036][ワクサドレッド]([x]<b>断末魔:</b>引かれた際「ワクサドレッド」を再度召喚するロウソク1枚を______自分のデッキに混ぜる。_)
#[DRG_037][フリック・スカイシヴ]([x]<b>雄叫び:</b>ミニオン1体と同名のミニオン全てを破壊する<i>（居場所は問わない）</i>。)
#[DRG_049][美味しいマロバルーン](<b>断末魔:</b>自分の手札のドラゴン1体に__+2/+2を付与する。)
#[DRG_050][心血注ぐ献身者](<b>急襲</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。)
#[DRG_054][ぽっちゃりチビドラゴン](<b>雄叫び:</b>カードを1枚引く。)
#[DRG_055][財宝荒らし]([x]<b>雄叫び:</b>自分の破壊された___武器1つを装備する。)
#[DRG_056][パラシュート・パイレート]([x]自分が海賊を手札から使用した後自分の手札から____このミニオンを召喚する。)
#[DRG_057][熱気球]([x]自分のターンの開始時体力+1を獲得する。)
#[DRG_058][ウィングコマンダー]([x]自分の手札のドラゴン1体につき__攻撃力+2を得る。)
#[DRG_059][ゴボグライダー技士]([x]<b>雄叫び:</b>自分の陣地にメカがいる場合+1/+1と<b>急襲</b>を獲得する。)
#[DRG_060][ファイアーホーク]([x]<b>雄叫び:</b>相手の手札1枚につき__攻撃力+1を獲得する。)
#[DRG_061][オートジャイロ](<b>急襲</b>、<b>疾風</b>)
#[DRG_062][ワームレストの浄術師]([x]<b>雄叫び:</b>自分のデッキの中立カード全てをランダムな自分のクラスのカードに変身させる。)
#[DRG_063][ドラゴンモーの密猟者](<b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。)
#[DRG_064][ズルドラクの儀式官]([x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__)
#[DRG_065][ヒポグリフ](<b>急襲</b>、<b>挑発</b>)
#[DRG_066][躱し身のキメラ](<b>猛毒</b>呪文とヒーローパワーの標的にならない。)
#[DRG_067][トロルのコウモリ騎兵](<b>雄叫び:</b>ランダムな敵のミニオン1体に__3ダメージを与える。)
#[DRG_068][生き息ドラゴンブレス](味方のミニオンは<b>凍結</b>しない。)
#[DRG_069][プレートブレイカー]([x]<b>雄叫び:</b>相手の装甲を破壊する。)
#[DRG_070][ドラゴンブリーダー](<b>雄叫び:</b>味方のドラゴン1体を選択する。そのコピー1体を自分の手札に追加する。)
#[DRG_071][悪運アホウドリ]([x]<b>断末魔:</b>相手のデッキに1/1の「アホウドリ」2体を混ぜる。)
#[DRG_072][スカイフィン](<b>雄叫び:</b>自分の手札にドラゴンがいる場合ランダムなマーロックを2体召喚する。)
#[DRG_073][躱し身のフェイウィング](呪文とヒーローパワーの標的にならない。)
#[DRG_074][擬装した飛行船]([x]<b>雄叫び:</b>次の自分のターンまで自身を除く味方のメカに<b>隠れ身</b>を付与する。)
#[DRG_075][コバルト・スペルキン]([x]<b>雄叫び:</b>自分のクラスのコスト1の呪文2枚を自分の手札に追加する。)
#[DRG_076][無貌の変性者](<b>急襲</b>、<b>雄叫び:</b>味方のミニオン1体をこのミニオンのコピーに変身させる。)
#[DRG_077][ウトガルドのグラップル狙撃手]([x]<b>雄叫び:</b>両プレイヤーはカードを1枚引く。それがドラゴンだった場合召喚する。)
#[DRG_078][爆雷]([x]自分のターンの開始時全てのミニオンに___5ダメージを与える。)
#[DRG_079][躱し身のワーム](<b>聖なる盾</b>、<b>急襲</b>呪文とヒーローパワーの標的にならない。)
#[DRG_081][スケイルライダー]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____2ダメージを与える。)
#[DRG_082][コボルトの棒ドロ](<b>雄叫び:</b>相手の武器を奪う。)
#[DRG_084][触手の脅異]([x]<b>雄叫び:</b>各プレイヤーはカードを1枚ずつ引く。それらの____コストを入れ替える。__)
#[DRG_086][クロマティックの卵]([x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！)
#[DRG_088][タタリガラス](自身を除く味方の「タタリガラス」1体につき攻撃力+3を得る。)
#[DRG_089][竜の女王アレクストラーザ]([x]<b>雄叫び:</b>_自分のデッキに重複するカードがない場合自身を除くランダムなドラゴン2体を自分の手札に追加する。____それらのコストは（1）になる。)
#[DRG_091][シュ＝マ]([x]自分のターンの終了時自分の陣地に1/1の「触手」を可能な限り召喚する。)
#[DRG_092][魔改造師]([x]自分がカードを引く度それをランダムな<b>レジェンド</b>ミニオンに変身させる。)
#[DRG_099][クロンクス・ドラゴンフーフ]([x]<b>雄叫び:</b>ガラクロンドを引く。自分が既にガラクロンドの場合ガラクロンドの大禍を引き起こす。)
#[DRG_213][双暴帝]([x]<b>雄叫び:</b>ランダムな敵のミニオン2体に_____4ダメージずつ与える。)
#[DRG_239][爆熱バトルメイジ]()
#[DRG_242][ガラクロンドの盾](<b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。)
#[DRG_247][刻まれし運命]([x]ダメージを受けていないキャラクター1体に$3ダメージを与える。ガラクロンドに<b>祈願</b>する。)
#[DRG_257][フリズ・キンドルルースト](<b>雄叫び:</b>自分のデッキのドラゴン全てのコストを（2）減らす。)
#[DRG_310][躱し身のドラコニッド](<b>挑発:</b>呪文とヒーローパワーの標的にならない。)
#[DRG_401][灰色の魔法使い]([x]<b>雄叫び:</b>次の自分のターンまで相手とヒーロー______パワーを交換する。_)
#[DRG_402][サスロヴァール]([x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのコピーを自分の手札、デッキ、陣地に_____それぞれ1体ずつ追加する。)
#[DRG_403][ブロートーチ妨害工作員](<b>雄叫び:</b>相手が次に使うヒーローパワーのコストは（3）。)
#[DS1_055][ダークスケイルの治療師](<b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。)
#[EX1_001][ライトウォーデン]([x]キャラクターが回復を受ける度に攻撃力+2を獲得する。)
#[EX1_002][黒騎士]([x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。)
#[EX1_004][若きプリーステス]([x]自分のターンの終了時自身を除くランダムな味方のミニオン1体に_____体力+1を付与する。)
#[EX1_005][大物ハンター]([x]<b>雄叫び:</b>攻撃力7以上のミニオン1体を破壊する。)
#[EX1_006][アラームロボ]([x]自分のターンの開始時このミニオンを自分の手札のランダムな　ミニオンと入れ替える。__)
#[EX1_007][苦痛の侍祭]([x]このミニオンがダメージを受ける度　カードを1枚引く。)
#[EX1_008][アージェントの従騎士](<b>聖なる盾</b>)
#[EX1_009][アングリーチキン]([x]ダメージを受けている間は___攻撃力+5を得る。)
#[EX1_010][ウォーゲンのスパイ](<b>隠れ身</b>)
#[EX1_011][ヴードゥーの呪術医](<b>雄叫び:</b>体力を#2回復する。)
#[EX1_012][ブラッドメイジ・サルノス]([x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。)
#[EX1_014][キング・ムクラ](<b>雄叫び:</b> 敵の手札に「バナナ」2枚を追加する。)
#[EX1_015][初級エンジニア](<b>雄叫び:</b> カードを1枚引く。)
#[EX1_016][シルヴァナス・ウィンドランナー]([x]<b>断末魔:</b>ランダムな敵のミニオン1体を味方にする。)
#[EX1_017][ジャングル・パンサー](<b>隠れ身</b>)
#[EX1_019][シャタード・サンの聖職者]([x]<b>雄叫び:</b>味方のミニオン1体に +1/+1を 付与する。)
#[EX1_020][スカーレット・クルセイダー](<b>聖なる盾</b>)
#[EX1_021][スロールマーの遠見師](<b>疾風</b>)
#[EX1_023][シルバームーンの守護兵](<b>聖なる盾</b>)
#[EX1_025][ミニドラゴン・メカニック]([x]<b>雄叫び:</b> 2/1のメカ・ミニドラゴンを[b]1体召喚する。)
#[EX1_028][ストラングルソーントラ](<b>隠れ身</b>)
#[EX1_029][レプラノーム]([x]<b>断末魔:</b> 敵のヒーローに　2ダメージを与える。)
#[EX1_032][サンウォーカー]([x]<b>挑発</b>、<b>聖なる盾</b>)
#[EX1_033][疾風のハーピィ](<b>疾風</b>)
#[EX1_043][トワイライト・ドレイク](<b>雄叫び:</b> 自分の手札1枚につき体力+1を獲得する。)
#[EX1_044][クエスト中の冒険者]([x]自分がカードを使う度、+1/+1を獲得する。)
#[EX1_045][古代の番人](攻撃できない。)
#[EX1_046][ダークアイアンのドワーフ]([x]<b>雄叫び:</b> このターンの間ミニオン1体に　攻撃力+2を付与する。)
#[EX1_048][スペルブレイカー]([x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。)
#[EX1_049][若き酒造大師](<b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。)
#[EX1_050][コールドライトの託宣師]([x]<b>雄叫び:</b> 各プレイヤーはカードを2枚ずつ引く。)
#[EX1_055][マナ中毒者]([x]自分が呪文を使う度そのターンの間攻撃力+2を獲得する。)
#[EX1_057][老練の酒造大師](<b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。)
#[EX1_058][サンフューリーの護衛]([x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。)
#[EX1_059][イカレた錬金術師]([x]<b>雄叫び:</b> ミニオン1体の攻撃力と体力を入れ替える。)
#[EX1_062][大いなるマーク・アイ]([x]<b>突撃:</b>戦場にいる他の_マーロック1体につき__攻撃力+1を得る。)
#[EX1_066][酸性沼ウーズ](<b>雄叫び:</b> 敵の武器を破壊する。)
#[EX1_067][アージェントの司令官]([x]<b>突撃</b>、<b>聖なる盾</b>)
#[EX1_076][ポケットサイズの召喚師](毎ターン最初に手札から使用するミニオンのコストが（1）減る。)
#[EX1_080][秘密の番人]([x]<b>秘策</b>が使用される度+1/+1を獲得する。)
#[EX1_082][マッドボンバー]([x]<b>雄叫び:</b>合計3ダメージを自身を除くキャラクターに____ランダムに振り分ける。)
#[EX1_083][ティンクマスター・オーバースパーク]([x]<b>雄叫び:</b> 自身以外のランダムなミニオン1体を5/5のデビルサウルスか_____1/1のリスに変身させる。_)
#[EX1_085][精神支配技士]([x]<b>雄叫び:</b> 戦場に敵のミニオンが4体以上いる場合ランダムな1体を自分の味方にする。)
#[EX1_089][魔力のゴーレム]([x]<b>雄叫び:</b>相手にマナクリスタルを1個付与する。)
#[EX1_093][アルガスの守護者](<b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。)
#[EX1_095][ガジェッツァンの競売人](自分が呪文を使う度カードを1枚引く。)
#[EX1_096][戦利品クレクレ君]([x]<b>断末魔:</b>カードを1枚引く。)
#[EX1_097][涜れしもの]([x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。)
#[EX1_100][探話士チョー](プレイヤーが呪文を使う度、もう1人のプレイヤーの手札にその呪文のコピーを追加する。)
#[EX1_102][破壊兵器](自分のターンの開始時ランダムな敵1体に2ダメージを与える。)
#[EX1_103][コールドライトの予言者]([x]<b>雄叫び:</b> 自身を除く味方のマーロックに_____体力+2を付与する。)
#[EX1_105][山の巨人](このカード以外の自分の手札1枚につきコストが（1）減る。)
#[EX1_110][ケーアン・ブラッドフーフ]([x]<b>断末魔:</b>4/5のベイン・ブラッドフーフを1体召喚する。)
#[EX1_112][ゲルビン・メカトルク](<b>雄叫び:</b> すばらしい発明品を1体召喚する。)
#[EX1_116][リロイ・ジェンキンス]([x]<b>突撃</b>、<b>雄叫び:</b> 敵の陣地に1/1のチビドラゴンを2体召喚する。)
#[EX1_124][腹裂き]([x]$2ダメージを与える。<b>コンボ:</b> 代わりに$4ダメージを与える。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_126][裏切り]([x]敵のミニオン1体を操り隣接するミニオンにダメージを与えさせる。)
#[EX1_128][隠蔽]([x]次の自分のターンまで味方のミニオン全てに<b>隠れ身</b>を付与する。)
#[EX1_129][ナイフの雨]([x]敵のミニオン全てに$1ダメージを与える。カードを1枚引く。)
#[EX1_131][デファイアスの親方]([x]<b>コンボ:</b>2/1のデファイアスの盗賊を1体召喚する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_133][地獄送りの刃]([x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_134][SI:7諜報員]([x]<b>コンボ:</b> 2ダメージを与える。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_137][脳天直撃]([x]敵のヒーローに$2ダメージを与える。<b>コンボ:</b> 次のターン、このカードを自分の手札に戻す。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_144][影隠れ]([x]味方のミニオン1体を自分の手札に戻す。そのミニオンのコストは（2）減る。)
#[EX1_145][段取り]([x]このターン自分が次に使用する呪文のコストが（2）減る。)
#[EX1_162][ダイアウルフ・リーダー](隣接するミニオンは攻撃力+1を得る。)
#[EX1_170][エンペラー・コブラ](<b>猛毒</b>)
#[EX1_182][失敬](他のクラスのランダムなカード1枚を自分の手札に追加する。)
#[EX1_186][SI:7潜入工作員]([x]<b>雄叫び:</b>ランダムな敵の___<b>秘策</b>1つを破壊する。)
#[EX1_187][魔力喰らい]([x]自分が呪文を使う度+2/+2を獲得する。)
#[EX1_188][荒野の口取り]([x]<b>雄叫び:</b>ランダムな獣を1体召喚する。)
#[EX1_189][ブライトウィング](<b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。)
#[EX1_190][大審問官ホワイトメイン](<b>雄叫び:</b>このターンに死亡した味方のミニオン全てを召喚する。)
#[EX1_191][病魔の運び手]([x]<b>雄叫び:</b>味方のミニオン1体に<b>猛毒</b>を付与する。)
#[EX1_249][バロン・ゲドン](自分のターンの終了時自身を除く全てのキャラクターに2ダメージを与える。)
#[EX1_278][ドス]([x]$1ダメージを与える。カードを1枚引く。)
#[EX1_283][フロスト・エレメンタル]([x]<b>雄叫び:</b> キャラクター1体を<b>凍結</b>させる。)
#[EX1_284][アジュア・ドレイク]([x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。)
#[EX1_298][炎の王ラグナロス](攻撃できない。自分のターンの終了時ランダムな敵1体に8ダメージを与える。)
#[EX1_390][トーレン・ウォリアー]([x]<b>挑発</b>ダメージを受けている間は___攻撃力+3を得る。)
#[EX1_393][アマニの狂戦士]([x]ダメージを受けている間は___攻撃力+3を得る。)
#[EX1_396][魔古山の番兵](<b>挑発</b>)
#[EX1_399][グルバシの狂戦士](このミニオンがダメージを受ける度攻撃力+3を獲得する。)
#[EX1_405][盾持ち](<b>挑発</b>)
#[EX1_412][激昂のウォーゲン]([x]ダメージを受けている間は攻撃力+1と__<b>疾風</b>を得る。)
#[EX1_506][マーロックのタイドハンター]([x]<b>雄叫び:</b> 1/1のマーロックの 偵察兵を1体召喚する。)
#[EX1_507][マーロックの戦隊長]([x]自身を除く味方のマーロックは攻撃力+2を得る。)
#[EX1_508][グリムスケイルの託宣師]([x]自身を除く味方のマーロックは攻撃力+1を得る。)
#[EX1_509][マーロックのタイドコーラー]([x]自分がマーロックを召喚する度___攻撃力+1を獲得する。)
#[EX1_522][埋伏の暗殺者]([x]<b>隠れ身</b>、<b>猛毒</b>)
#[EX1_556][刈入れゴーレム]([x]<b>断末魔:</b> 2/1の壊れかけのゴーレムを1体召喚する。)
#[EX1_557][ナット・ペイグル]([x]自分のターンの開始時50%の確率でカード1枚を余分に引く。)
#[EX1_558][ハリソン・ジョーンズ](<b>雄叫び:</b> 敵の武器を破壊しその耐久度に等しい枚数のカードを引く。)
#[EX1_560][ノズドルム]([x]両プレイヤーの1ターンの持ち時間が15秒だけになる。)
#[EX1_561][アレクストラーザ]([x]<b>雄叫び:</b>ヒーロー1人の残り__体力を15にする。)
#[EX1_562][オニクシア]([x]<b>雄叫び:</b>自分の陣地が満員になる数の1/1のチビドラゴンを召喚する。)
#[EX1_563][マリゴス](<b>呪文ダメージ+5</b>)
#[EX1_564][無貌の操り手](<b>雄叫び:</b> ミニオン1体を選択しそのミニオンのコピーに変化する。)
#[EX1_572][イセラ]([x]自分のターンの終了時夢カード1枚を自分の手札に追加する。)
#[EX1_577][魔獣]([x]<b>断末魔:</b> 3/3のフィンクル・アインホルンを1体敵の陣地に召喚する。)
#[EX1_581][昏倒]([x]敵のミニオン1体を[b]相手の手札に[b]戻す。)
#[EX1_582][ダラランのメイジ](<b>呪文ダメージ+1</b>)
#[EX1_583][エルーンのプリーステス](<b>雄叫び:</b>自分のヒーローの体力を#4回復する。)
#[EX1_584][老練のメイジ]([x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。)
#[EX1_586][海の巨人](戦場にいるミニオン1体につきコストが（1）減る。)
#[EX1_590][ブラッドナイト]([x]<b>雄叫び:</b> 全てのミニオンは<b>聖なる盾</b>を失う。失われた聖なる盾1つにつき+3/+3を獲得する。)
#[EX1_593][ナイトブレード]([x]<b>雄叫び: </b>敵のヒーローに3ダメージを与える。)
#[EX1_595][カルトの教祖]([x]味方のミニオンが死亡した後____カードを1枚引く。)
#[EX1_597][インプ使い]([x]自分のターンの終了時このミニオンに1ダメージを与え1/1のインプを1体召喚する。)
#[EX1_613][エドウィン・ヴァンクリーフ](<b>コンボ:</b>このターン中で先に使用されたカード1枚につき+2/+2を獲得する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[EX1_614][ザヴィウス]([x]自分がカードを手札から使用した後2/1のサテュロスを1体召喚する。)
#[EX1_616][マナ・レイス](全てのミニオンのコストが（1）増える。)
#[EX1_620][溶岩の巨人]([x]自分のヒーローが受けているダメージ1につき_____コストが（1）減る。)
#[FP1_001][エサゾンビ]([x]<b>断末魔:</b>敵のヒーローの体力を#5回復する。)
#[FP1_002][呪われた蜘蛛](<b>断末魔:</b> 1/1の亡霊蜘蛛を2体召喚する。)
#[FP1_003][反響ウーズ](<b>雄叫び:</b> このターンの終了時にこのミニオンと全く同じコピーを1体召喚する。)
#[FP1_004][マッドサイエンティスト]([x]<b>断末魔:</b> 自分のデッキにある_______<b>秘策</b>1枚を準備する。)
#[FP1_005][ナクスラーマスの亡霊](<b>隠れ身:</b> 自分のターンの開始時+1/+1を獲得する。)
#[FP1_007][ネルビアンの卵](<b>断末魔:</b> 4/4のネルビアンを1体召喚する。)
#[FP1_008][亡霊騎士](呪文とヒーローパワーの標的にならない。)
#[FP1_009][デスロード]([x]<b>挑発、断末魔:</b> 相手プレイヤーはデッキからミニオン_______1体を陣地に置く。_)
#[FP1_010][マイエクスナ](<b>猛毒</b>)
#[FP1_012][ヘドロゲッパー]([x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。)
#[FP1_013][ケルスザード]([x]各ターンの終了時そのターンに死亡した味方のミニオン全てを召喚する。)
#[FP1_014][スタラグ](<b>断末魔:</b> この対戦中にフューゲンも死亡した場合、サディアスを召喚する。)
#[FP1_015][フューゲン]([x]<b>断末魔:</b> この対戦中にスタラグも死亡していた場合____サディアスを召喚する。)
#[FP1_016][泣き叫ぶ魂]([x]<b>雄叫び: </b>自身を除く味方のミニオンを_____<b>沈黙</b>させる。)
#[FP1_017][ネルバー・ウェブロード](全ての<b>雄叫び</b>を持つミニオンのコストが（2）増える。)
#[FP1_024][不安定なグール]([x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。)
#[FP1_026][アヌバー・アンブッシャー]([x]<b>断末魔:</b> ランダムな味方のミニオン1体を_______自分の手札に戻す。_)
#[FP1_027][石肌のガーゴイル]([x]自分のターンの開始時このミニオンの体力を上限まで回復する。)
#[FP1_028][墓掘り人]([x]自分が<b>断末魔</b>を持つミニオンを召喚する度__攻撃力+1を獲得する。)
#[FP1_029][踊る剣]([x]<b>断末魔:</b>相手はカードを1枚引く。)
#[FP1_030][ロウゼブ](<b>雄叫び:</b> 次のターン敵の呪文のコストが（5）増える。)
#[FP1_031][バロン・リーヴェンデア]([x]味方のミニオンの__<b>断末魔</b>は2回発動する。)
#[GIL_117][涜れしウォーゲン]([x]自分のターンの終了時自身を除くダメージを受けているミニオン全てに2ダメージを与える。)
#[GIL_118][キジル博士]([x]<b>断末魔:</b>自分のヒーローの体力を#8回復する。)
#[GIL_119][大釜のエレメンタル]([x]自身を除く味方のエレメンタルは__攻撃力+2を得る。)
#[GIL_120][怒れるエティン](<b>挑発</b>)
#[GIL_121][ダークマイア・ムーンキン](<b>呪文ダメージ+2</b>)
#[GIL_124][苔むしたモノノケ]([x]<b>雄叫び:</b>自身を除く攻撃力2以下のミニオンを全て破壊する。)
#[GIL_125][いかれ帽子屋]([x]<b>雄叫び:</b>自身を除くミニオンに帽子を3個ランダムに投げる。帽子はそれぞれ+1/+1を付与する。)
#[GIL_143][獰猛なスケイルハイド](<b>生命奪取</b>、<b>急襲</b>)
#[GIL_198][アザリナ・ソウルシーフ]([x]<b>雄叫び:</b>自分の手札全てを相手の手札全てのコピーに置き換える。)
#[GIL_201][カボチャ農家]([x]<b>生命奪取</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GIL_202][ギルニーアスの近衛兵]([x]<b>聖なる盾</b>、<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GIL_207][幽霊民兵](<b>木霊</b>、<b>挑発</b>)
#[GIL_212][鴉使い]([x]<b>雄叫び:</b>ランダムなコスト1のミニオン2体を自分の手札に追加する。)
#[GIL_213][毛むくじゃらのミスティック]([x]<b>雄叫び:</b>ランダムなコスト2の___ミニオン1体を各プレイヤーの手札に追加する。)
#[GIL_506][卑劣な一撃]([x]<b>木霊</b>ミニオン1体に$2ダメージを与える。)
#[GIL_510][ミストレイス]([x]自分が<b>木霊</b>を持つカードを手札から使用する度____+1/+1を獲得する。)
#[GIL_513][迷える魂](<b>断末魔:</b>味方のミニオン全てに攻撃力+1を__付与する。)
#[GIL_526][ワームガード]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。)
#[GIL_527][フェルソウルの異端審問官](<b>生命奪取</b>、<b>挑発</b>)
#[GIL_528][俊足な使者]([x]<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GIL_529][スペルシフター]([x]<b>呪文ダメージ+1</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。)
#[GIL_534][ヘンチ・クランのゴロツキ]([x]自分のヒーローが攻撃した後、このミニオンに+1/+1を付与する。)
#[GIL_557][呪われた漂流者]([x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[GIL_558][沼ビル](<b>生命奪取</b>)
#[GIL_561][ブラックワルド・ピクシー]([x]<b>雄叫び:</b>自分のヒーローパワーを再度使用可能にする。)
#[GIL_578][アッシュモア伯爵夫人]([x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。)
#[GIL_581][サンドバインダー]([x]<b>雄叫び:</b>自分のデッキからエレメンタル_を1体引く。)
#[GIL_584][ウィッチウッドの笛吹き]([x]<b>雄叫び:</b>自分のデッキから最もコストが低い____ミニオンを1体引く。)
#[GIL_598][テス・グレイメイン]([x]<b>雄叫び:</b>この対戦で自分が手札から使用した他のクラスのカード全てを再度使用する<i>（対象はランダムに選択される）</i>。)
#[GIL_601][スケイルワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。)
#[GIL_614][ヴードゥー人形]([x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。)
#[GIL_616][裂けるフェスタールート]([x]<b>断末魔:</b>2/2の「裂けた若木」を2体召喚する。)
#[GIL_620][人形師ドリアン]([x]自分がミニオンを引く度、そのミニオンの1/1のコピーを1体召喚する。)
#[GIL_622][ライフドリンカー]([x]<b>雄叫び:</b>敵のヒーローに3ダメージを与える。自分のヒーローの体力を#3回復する。)
#[GIL_623][ウィッチウッドのグリズリー]([x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。)
#[GIL_624][ナイトプロウラー]([x]<b>雄叫び:</b>戦場に他のミニオンがいない場合、+3/+3を獲得する。)
#[GIL_646][時計仕掛けの自動人形]([x]自分のヒーローパワーが与えるダメージと回復の効果を2倍にする。)
#[GIL_648][ギルニーアスの警部](<b>雄叫び:</b>敵の<b>秘策</b>全てを破壊する。)
#[GIL_667][朽ちかけたアップルバウム]([x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。)
#[GIL_672][亡霊カトラス]([x]<b>生命奪取</b>自分が他のクラスのカードを手札から使用__する度、耐久度+1を獲得する。)
#[GIL_677][貌を蒐めるもの]([x]<b>木霊</b>、<b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。)
#[GIL_680][胡桃のスプライト](<b>木霊</b>)
#[GIL_681][悪夢の融合体]([x]<i>これはエレメンタル、メカ、悪魔、マーロック、ドラゴン、獣、海賊、トーテムである。</i>)
#[GIL_682][マックハンター]([x]<b>急襲</b>、<b>雄叫び:</b>相手の陣地に2/1の「マックリング」_を2体召喚する。)
#[GIL_683][沼地のドレイク]([x]<b>雄叫び:</b>相手の陣地に<b>猛毒</b>を持つ2/1の「ドレイクスレイヤー」を1体召喚する。)
#[GIL_687][賞金首]([x]ミニオン1体に$3ダメージを与える。これにより対象が死亡した場合、自分の手札に「コイン」1枚を追加する。)
#[GIL_692][ゲン・グレイメイン]([x]<b>対戦開始時:</b>自分のデッキに偶数コストのカードしかない場合、開始時の自分のヒーローパワーのコストが（1）になる。)
#[GIL_696][掏り取り]([x]<b>木霊</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。)
#[GIL_809][眠るスチームロボ](<b>挑発</b>)
#[GIL_815][悪意の銀行家]([x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのコピー1体を___自分のデッキに混ぜる。)
#[GIL_816][沼のドラゴンの卵]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[GIL_819][魔女の大釜]([x]味方のミニオンが死亡した後、ランダムなシャーマンの呪文1枚を______自分の手札に追加する。)
#[GIL_826][月を食らうものバク]([x]<b>対戦開始時:</b>自分のデッキに奇数コストのカードしかない場合自分のヒーローパワーをアップグレードする。)
#[GIL_827][ブリンク・フォックス]([x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。)
#[GIL_902][人斬りバッカニーア](<b>コンボ:</b>自分の武器に攻撃力+1を__付与する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[GVG_006][メカワーパー](自分のメカのコストが（1）減る。)
#[GVG_013][コグマスター](味方にメカがいる場合、攻撃力+2。)
#[GVG_016][フェル・リーヴァー](相手がカードを使う度自分のデッキの上から3枚のカードを捨てる。)
#[GVG_022][ティンカーの刃研ぎ油](自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[GVG_023][ゴブリン式全自動散髪機]([x]<b>雄叫び:</b> 自分の武器に攻撃力+1を__付与する。)
#[GVG_024][コグマスターのレンチ](味方にメカがいる場合攻撃力+2。)
#[GVG_025][隻眼のチート]([x]自分が海賊を召喚する度、<b>隠れ身</b>を獲得する。)
#[GVG_027][鉄の師匠]([x]自分のターンの終了時自身を除く味方のメカ1体に+2/+2を付与する。)
#[GVG_028][商大公ガリーウィックス]([x]相手が呪文を使う度自分はその呪文のコピー1枚を獲得し、相手は「ガリーウィックスの______コイン」1枚を獲得する。_)
#[GVG_044][クモ戦車]()
#[GVG_047][サボタージュ]([x]ランダムな敵のミニオン1体を破壊する。<b>コンボ:</b> さらに敵の武器を破壊する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[GVG_064][パドルストンパー]()
#[GVG_065][オーガの暴れん坊]([x]50%の確率で指定していない敵を攻撃する。)
#[GVG_067][ストーンスプリンター・トログ]([x]相手が呪文を使う度攻撃力+1を獲得する。)
#[GVG_068][バーリー・ロックジョー・トログ]([x]相手が呪文を使う度攻撃力+2を獲得する。)
#[GVG_069][骨董品のヒールロボ](<b>雄叫び:</b>自分のヒーローの体力を#8回復する。)
#[GVG_070][老練船乗り]()
#[GVG_071][迷子のトールストライダー]()
#[GVG_074][ケザンのミスティック](<b>雄叫び:</b> 敵のランダムな<b>秘策</b>1つを自分のものにする。)
#[GVG_075][艦載砲](自分が海賊を召喚した後ランダムな敵1体に2ダメージを与える。)
#[GVG_076][爆発ヒツジ](<b>断末魔:</b> 全てのミニオンに2ダメージを与える。)
#[GVG_078][メカ・イェティ](<b>断末魔:</b> 各プレイヤーに<b>スペアパーツ</b>カード1枚を与える。)
#[GVG_079][フォース・タンクMAX](<b>聖なる盾</b>)
#[GVG_081][ギルブリン・ストーカー](<b>隠れ身</b>)
#[GVG_082][ゼンマイ仕掛けのノーム](<b>断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。)
#[GVG_084][飛行マシーン](<b>疾風</b>)
#[GVG_085][マジウザ・オ・トロン](<b>挑発</b><b>聖なる盾</b>)
#[GVG_088][オーガ・ニンジャ](<b>隠れ身:</b>50%の確率で、指定していない敵を攻撃する。)
#[GVG_089][イルミネイター](自分のターンの終了時に<b>秘策</b>が準備されている場合自分のヒーローの体力を#4回復する。)
#[GVG_090][マッダーボンバー]([x]<b>雄叫び:</b>合計6ダメージを自身を除くキャラクターに____ランダムに振り分ける。)
#[GVG_091][アーケン・ヌリファイアーX-21](<b>挑発:</b>呪文とヒーローパワーの標的にならない。)
#[GVG_092][ノームの実験者]([x]<b>雄叫び:</b> カードを1枚引く。そのカードがミニオンだった場合、そのカードを________ニワトリに変身させる。__)
#[GVG_093][ターゲット・ダミー](<b>挑発</b>)
#[GVG_094][ジーヴス]([x]各プレイヤーは自分のターンの終了時に手札が3枚になるまでカードを引く。)
#[GVG_095][ゴブリン戦闘工兵](相手の手札が6枚以上ある場合、攻撃力+4を持つ。)
#[GVG_096][手動操縦のシュレッダー](<b>断末魔:</b> ランダムなコスト2のミニオン1体を召喚する。)
#[GVG_097][リトル・エクソシスト]([x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_)
#[GVG_098][ノームレガン歩兵]([x]<b>突撃</b>、<b>挑発</b>)
#[GVG_099][ボム・ロバー](<b>雄叫び:</b> ランダムな敵のミニオン1体に4ダメージを与える。)
#[GVG_102][ティンカータウンの技術者](<b>雄叫び:</b> 味方にメカがいる場合+1/+1を獲得しさらに自分の手札に<b>スペアパーツ</b>1枚を追加する。)
#[GVG_103][マイクロマシーン]([x]各ターンの開始時攻撃力+1を_獲得する。)
#[GVG_104][ホブゴブリン]([x]自分が攻撃力1のミニオンを場に出す度そのミニオンに______+2/+2を付与する。)
#[GVG_105][手動操縦のスカイ・ゴーレム](<b>断末魔:</b> ランダムなコスト4のミニオン1体を召喚する。)
#[GVG_106][ジャンクロボ]([x]味方のメカが死ぬ度+2/+2を獲得する。)
#[GVG_107][エンハンス・オ・メカーノ](<b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>)
#[GVG_108][リコンボビュレイター]([x]<b>雄叫び:</b> 味方のミニオン1体を、ランダムな同コストのミニオンに変身させる。)
#[GVG_109][ミニ・メイジ]([x]<b>呪文ダメージ+1</b><b>隠れ身</b>)
#[GVG_110][ドクター・ブーム](<b>雄叫び:</b> 1/1のブームロボを2体召喚する。<i>警告: ロボは爆発する場合がある。</i>)
#[GVG_111][ミミロン・ヘッド]([x]自分のターンの開始時味方にメカが3体以上いる場合それらは破壊されその後合体してV-07-TR-0Nとなる。)
#[GVG_112][モゴール・ジ・オーガ](全てのミニオンは、50%の確率で指定していない敵を攻撃する。)
#[GVG_113][エネミーリーパー4000](攻撃対象のミニオンと隣接するミニオンにもダメージを与える。)
#[GVG_114][スニードの旧型シュレッダー](<b>断末魔:</b> ランダムな<b>レジェンド</b>のミニオン1体を召喚する。)
#[GVG_115][トッシュリー]([x]<b>雄叫び、断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。)
#[GVG_116][メカジニア・サーマプラッグ](敵のミニオンが死ぬ度に、レプラノームを1体召喚する。)
#[GVG_117][ガズロウ]([x]自分がコスト1の呪文を使う度、ランダムなメカ1体を自分の手札に追加する。)
#[GVG_118][アーシネイター・トログザー](相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。)
#[GVG_119][ブリングトロン3000](<b>雄叫び:</b> 各プレイヤーはランダムな武器を装備する。)
#[GVG_120][ヒーメット・ネッシングウェアリー](<b>雄叫び:</b> 獣1体を破壊する。)
#[GVG_121][ゼンマイ仕掛けの巨人](敵の手札1枚につき、コストが（1）減る。)
#[ICC_018][ぶんどり幽霊船員]([x]<b>雄叫び:</b>自分の武器の値に等しい攻撃力と　体力を獲得する。)
#[ICC_019][骸骨術師]([x]<b>断末魔:</b>今が相手のターンの場合8/8のスケルトンを1体召喚する。)
#[ICC_023][スノーフリッパー・ペンギン]()
#[ICC_025][ガラガラガイコツ]([x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。)
#[ICC_026][非情の死霊術師]([x]<b>雄叫び:</b>1/1のスケルトンを2体召喚する。)
#[ICC_027][ボーン・ドレイク]([x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。)
#[ICC_028][サンボーン・ヴァルキル]([x]<b>雄叫び:</b>隣接するミニオンに　体力+2を付与する。)
#[ICC_029][コバルト・スケイルベイン]([x]自分のターンの終了時自身を除くランダムな味方のミニオン1体に_____攻撃力+3を付与する。)
#[ICC_031][ナイトハウラー](このミニオンがダメージを受ける度攻撃力+2を獲得する。)
#[ICC_032][毒術師](<b>猛毒</b>)
#[ICC_065][ボーン・バロン](<b>断末魔:</b>1/1のスケルトン2体を自分の手札に追加する。)
#[ICC_067][ヴライグール]([x]<b>断末魔:</b>今が相手のターンの場合2/2のグールを1体召喚する。)
#[ICC_092][アケラスの古残兵](<b>雄叫び:</b>味方のミニオン1体に攻撃力+1を付与する。)
#[ICC_093][タスカーの漁師]([x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。)
#[ICC_094][フォールン・サンの聖職者]([x]<b>雄叫び:</b>味方のミニオン1体に　+1/+1を付与する。)
#[ICC_096][タタラボッチ](<b>雄叫び:</b>自分の手札の武器を全て破棄しそれらの攻撃力と耐久度を獲得する。)
#[ICC_097][ダイダラ墓地]([x]自分の武器が破壊される度　+1/+1を獲得する。)
#[ICC_098][墓に潜むもの]([x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。)
#[ICC_099][涜れし爆弾](<b>断末魔:</b>味方のミニオン全てに5ダメージを与える。)
#[ICC_201][骰は投げられた]([x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。)
#[ICC_220][デッドスケイル・ナイト](<b>生命奪取</b>)
#[ICC_221][吸血毒]([x]このターンの間自分の武器に<b>生命奪取</b>を付与する。)
#[ICC_233][ドゥーメラン]([x]ミニオン1体に目がけて自分の武器を投げる。武器はダメージを与えた後自分の手札に戻る。)
#[ICC_240][ルーン鍛冶場のヌシ]([x]自分のターン中自分の武器は耐久度を失わない。)
#[ICC_257][死体蘇生者]([x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。)
#[ICC_314][リッチキング]([x]<b>挑発</b>自分のターンの終了時ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。)
#[ICC_466][サロナイト鉱山の奴隷]([x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。)
#[ICC_467][ネルビアンの説凶師]([x]<b>雄叫び:</b>味方のミニオン1体にこのターンの間<b>無敵</b>を付与する。)
#[ICC_468][悲惨な農夫]([x]このミニオンが攻撃する度敵のヒーローに_____2ダメージを与える。)
#[ICC_700][ハッピーグール](このターンに自分のヒーローが回復を受けた場合コスト（0）。)
#[ICC_701][待ち伏せのガイスト](<b>雄叫び:</b>両プレイヤーの手札とデッキのコスト1の呪文を全て破壊する。)
#[ICC_702][浅めの墓穴堀り](<b>断末魔:</b><b>断末魔</b>を持つランダムなミニオン1体を自分の手札に追加する。)
#[ICC_705][ボーンメア]([x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。)
#[ICC_706][ネルビアンの解絡師](呪文のコストが（2）増える。)
#[ICC_809][疫病科学者]([x]<b>コンボ:</b>味方のミニオン1体に<b>猛毒</b>を付与する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[ICC_810][斧死なる断罪者]([x]<b>雄叫び:</b>自分の手札の<b>生命奪取</b>を持つランダムなミニオン1体に+2/+2を付与する。)
#[ICC_811][リリアン・ヴォス]([x]<b>雄叫び:</b>自分の手札の呪文全てを<i>相手のクラスの</i>ランダムな呪文と置き換える。)
#[ICC_812][ミートワゴン]([x]<b>断末魔:</b>このミニオンより攻撃力が低いミニオンを1体自分のデッキから召喚する。)
#[ICC_850][シャドウブレード]([x]<b>雄叫び:</b>自分のヒーローはこのターンの間<b>無敵</b>。)
#[ICC_851][ケレセス公爵]([x]<b>雄叫び:</b>自分のデッキにコスト2のカードがない場合、自分のデッキのミニオン全てに+1/+1を付与する。)
#[ICC_852][タルダラム公爵]([x]<b>雄叫び:</b>自分のデッキにコスト3のカードがない場合選択したミニオンの3/3のコピーに変身する。)
#[ICC_853][ヴァラナール公爵]([x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。)
#[ICC_854][アーファス](<b>断末魔:</b>ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。)
#[ICC_855][ヒルドニル・フロストライダール](<b>雄叫び:</b>自身を除く味方のミニオンを<b>凍結</b>させる。)
#[ICC_856][スペルウィーヴァー](<b>呪文ダメージ+2</b>)
#[ICC_900][壊死のガイスト]([x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。)
#[ICC_901][ドラッカリの呪い師]([x]自分のターンの終了時に発動する効果は2回発動する。)
#[ICC_902][マインドブレーカー](ヒーローパワーは使用不能になる。)
#[ICC_904][骸骨の魔女]([x]<b>雄叫び:</b>このターンに死亡したミニオン1体につき　+1/+1を獲得する。)
#[ICC_905][吸血蟲](<b>生命奪取</b>)
#[ICC_910][略奪の亡霊]([x]<b>コンボ:</b>このターン中で先に使用したカードの枚数に等しいダメージを与える。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[ICC_911][号泣のバンシー]([x]自分がカードを使う度自分のデッキの上から3枚のカードを除去する。)
#[ICC_912][躯の駆り手]([x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。)
#[ICC_913][穢れし狂信者](<b>聖なる盾</b><b>呪文ダメージ+1</b>)
#[KAR_011][気取り屋の俳優](<b>挑発</b>)
#[KAR_029][ルーンの卵](<b>断末魔:</b>カードを1枚引く。)
#[KAR_030a][食糧庫蜘蛛](<b>雄叫び:</b>1/3の蜘蛛を1体召喚する。)
#[KAR_033][ブック・ワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力3以下の敵の______ミニオン1体を破壊する。_)
#[KAR_036][魔力異常体]([x]自分が呪文を使う度このミニオンに体力+1を付与する。)
#[KAR_037][番鳥](<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。)
#[KAR_041][堀に潜むもの](<b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。)
#[KAR_044][モローズ]([x]<b>隠れ身</b>自分のターンの終了時1/1の家令を1体召喚する。)
#[KAR_061][キュレーター]([x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。)
#[KAR_062][ネザースパイトの歴史家]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合____ドラゴン1体を<b>発見</b>する。)
#[KAR_069][怪盗紳士]([x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。)
#[KAR_070][イセリアルの売人]([x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合それらのコストを（2）減らす。)
#[KAR_094][殺意のフォーク](<b>断末魔:</b>3/2の武器1枚を自分の手札に追加する。)
#[KAR_095][動物園ロボ]([x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+1/+1を付与する。)
#[KAR_096][マルシェザール公爵]([x]<b>対戦開始時:</b>自分のデッキに<b>レジェンド</b>ミニオンを5体追加する。)
#[KAR_097][ガーディアン・メディヴ]([x]<b>雄叫び:</b>ガーディアンの大杖__アティシュを装備する。)
#[KAR_114][バーンズ](<b>雄叫び:</b>自分のデッキのランダムなミニオンの1/1のコピーを[x]1体召喚する。)
#[KAR_702][動物園の奇術師]([x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+2/+2を付与する。)
#[KAR_710][魔力細工師](<b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。)
#[KAR_711][魔力の巨人]([x]この対戦で自分が使用した呪文1回につき_____コストが（1）減る。)
#[KAR_712][ヴァイオレット・アイの幻術師](自分のターン中[x]自分のヒーローは<b>無敵</b>。)
#[LOE_010][ピットスネーク](<b>猛毒</b>)
#[LOE_011][レノ・ジャクソン]([x]<b>雄叫び:</b>自分のデッキに重複するカードがない場合自分のヒーローの体力を完全に回復する。)
#[LOE_012][墓荒らし](<b>断末魔:</b> 自分の手札に「コイン」1枚を追加する。)
#[LOE_019][掘り起こされたラプター]([x]<b>雄叫び:</b> 味方のミニオン1体を選択する。そのミニオンの____<b>断末魔</b>の能力をコピーする。)
#[LOE_029][宝飾のスカラベ]([x]<b>雄叫び:</b> コスト3の　カード1枚を<b>発見</b>する。)
#[LOE_038][ナーガの海の魔女](自分のカードのコストは（5）。)
#[LOE_039][ゴリラロボA-3]([x]<b>雄叫び:</b>味方に別のメカがいる場合メカ1体を<b>発見</b>する。)
#[LOE_046][巨大ガマ](<b>断末魔:</b> ランダムな敵1体に1ダメージを与える。)
#[LOE_047][墓守蜘蛛](<b>雄叫び:</b> 獣1体を<b>発見</b>する。)
#[LOE_053][西風のジニー]([x]自分がこのミニオンを除く、味方のミニオンに呪文を使用した後、その呪文をコピーし、このミニオンに対して使用する。)
#[LOE_061][アヌビサス・センチネル]([x]<b>断末魔:</b>ランダムな味方のミニオン1体に____+3/+3を付与する。)
#[LOE_073][デビルサウルスの化石](<b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。)
#[LOE_076][サー・フィンレー・マルグルトン](<b>雄叫び:</b>新たな基本ヒーローパワー1つを<b>発見</b>する。)
#[LOE_077][ブラン・ブロンズビアード](味方の<b>雄叫び</b>は2回発動する。)
#[LOE_079][エリーズ・スターシーカー]([x]<b>雄叫び:</b> 自分のデッキに「黄金のサルへの地図」1枚を混ぜる。)
#[LOE_086][召喚石](自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。)
#[LOE_089][ふらつくこびと達](<b>断末魔:</b> 2/2のこびとを3体召喚する。)
#[LOE_092][大怪盗ラファーム](<b>雄叫び:</b> 強力な秘宝を1つ<b>発見</b>する。)
#[LOE_107][不気味な像]([x]戦場に他のミニオンがいると攻撃できない。)
#[LOE_110][古代のシェード]([x]<b>雄叫び:</b>自分のデッキに「古代の呪い」1枚を混ぜる。「古代の呪い」を引くと_____自分が7ダメージを受ける。)
#[LOEA10_3][マーロック・タイニーフィン]()
#[LOOT_026][ファルドライ・ストライダー]([x]<b>雄叫び:</b> 自分のデッキに待ち伏せ！3枚を混ぜる。待ち伏せ！を引いた際自分の陣地に4/4のクモを1体召喚する。)
#[LOOT_033][大洞窟のキラキラ拾い]([x]<b>雄叫び:</b>自分のデッキから武器を1枚引く。)
#[LOOT_069][下水さらい]([x]<b>雄叫び:</b>2/3の「巨大ネズミ」を1体召喚する。)
#[LOOT_111][スコーピ・オ・マティック](<b>雄叫び:</b>攻撃力1以下のミニオン1体を破壊する。)
#[LOOT_117][蝋のエレメンタル](<b>挑発</b><b>聖なる盾</b>)
#[LOOT_118][漆黒のドラゴン鍛冶](<b>雄叫び:</b>自分の手札のランダムな武器1つのコストを（2）減らす。)
#[LOOT_122][腐蝕ヘドロ](<b>雄叫び:</b>敵の武器を破壊する。)
#[LOOT_124][孤高の勇者]([x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。)
#[LOOT_125][石肌のバジリスク](<b>聖なる盾</b><b>猛毒</b>)
#[LOOT_130][魔力の暴帝]([x]このターンにコスト（5）以上の呪文を使用していた場合コスト（0）。)
#[LOOT_131][グリーン・ジェリー]([x]自分のターンの終了時<b>挑発</b>を持つ1/2のウーズを1体召喚する。)
#[LOOT_132][ドラゴンスレイヤー](<b>雄叫び:</b>ドラゴン1体に6ダメージを与える。)
#[LOOT_134][牙を剥く宝箱]([x]自分のターンの開始時このミニオンの__攻撃力を4にする。)
#[LOOT_136][潜む悪鬼](<b>隠れ身</b>自身を除く味方のミニオンは攻撃力+1を得る。)
#[LOOT_137][眠れるドラゴン](<b>挑発</b>)
#[LOOT_144][護宝のドラゴン]([x]<b>断末魔:</b>相手に「コイン」2枚を与える。)
#[LOOT_149][回廊漁り蟲]([x]このカードが手札にある間ミニオンが死ぬ度コストが（1）減る。)
#[LOOT_150][ファーボルグの苔編み師]([x]<b>雄叫び:</b>味方のミニオン1体を__6/6のエレメンタルに__変身させる。)
#[LOOT_152][賑やかな吟遊詩人](<b>雄叫び:</b>自身を除く味方のミニオンに体力+1を付与する。)
#[LOOT_153][ヴァイオレット・ヴルム](<b>断末魔:</b>1/1の「芋虫」を7体召喚する。)
#[LOOT_154][ジャリッパナの騎士]([x]<b>雄叫び:</b>ランダムなコスト1のミニオン1体を____相手の陣地に召喚する。)
#[LOOT_161][肉食キューブ]([x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。)
#[LOOT_165][ソニア・シャドウダンサー](味方のミニオンが死亡した後、そのミニオンの1/1のコピーを自分の手札に追加する。そのカードのコストは（1）。)
#[LOOT_167][菌術師]([x]<b>雄叫び:</b>隣接するミニオンに__+2/+2を付与する。)
#[LOOT_184][シルバーヴァンガード]([x]<b>断末魔:</b>コスト8のミニオンを1体<b>招集</b>する。)
#[LOOT_193][きらめく駿馬]([x]自分のヒーローパワーか呪文でしか____標的にできない。)
#[LOOT_204][九死一生](<b>秘策:</b>味方のミニオンが死亡した時、そのミニオン1体を自分の手札に戻す。そのコストは（2）減る。)
#[LOOT_210][突然の裏切り](<b>秘策:</b>ミニオンが自分のヒーローを攻撃した時、代わりにそのミニオンに隣接する誰かを攻撃する。)
#[LOOT_211][エルフの吟遊楽人]([x]<b>コンボ:</b>自分のデッキから__ミニオンを2体引く。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[LOOT_214][雲隠れ](<b>秘策:</b>自分のヒーローがダメージを受けた後このターンの間<b>無敵</b>になる。)
#[LOOT_218][獰猛なクッチャベラー](このミニオンがヒーローを攻撃した後、自分の手札にこのミニオンのコピー1枚を追加する。)
#[LOOT_233][呪われた門弟]([x]<b>断末魔:</b>5/1のレヴナントを1体召喚する。)
#[LOOT_258][ダイアモール]()
#[LOOT_291][キノコ酒造師](<b>雄叫び:</b>体力を#4回復する。)
#[LOOT_315][トログのキノコ食い]([x]<b>挑発</b>、<b>猛毒</b>)
#[LOOT_347][コボルトの弟子]([x]<b>雄叫び:</b>合計3ダメージを敵にランダムに振り分ける。)
#[LOOT_357][狐のマリン]([x]<b>雄叫び:</b>相手の陣地に0/8の宝箱を1個召喚する。____<i>(破壊するとお宝入手！)_</i>)
#[LOOT_375][ギルド募集係](<b>雄叫び:</b>コスト（4）以下のミニオンを1体<b>招集</b>する。)
#[LOOT_382][コボルトのモンク](自分のヒーローは呪文とヒーローパワーの標的にならない。)
#[LOOT_383][飢えているエティン](<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。)
#[LOOT_388][キノコの呪い師](<b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。)
#[LOOT_389][クズ拾いのコボルト](<b>雄叫び:</b>自分の破壊された武器1つを自分の手札に戻す。)
#[LOOT_394][ワメキノコ]([x]自分のターンの終了時ランダムなコスト1のミニオン1体を召喚する。)
#[LOOT_412][コボルトの幻術師]([x]<b>断末魔:</b>自分の手札からミニオン1体の1/1のコピーを1体召喚する。)
#[LOOT_413][装甲虫](<b>断末魔:</b>装甲を3獲得する。)
#[LOOT_414][記録保管大臣]([x]自分のターンの終了時自分のデッキにある呪文1つを使用する。<i>__（対象はランダムに選択）</i>)
#[LOOT_503][オニキスの小呪文石]([x]ランダムな敵のミニオン1体を破壊する。@<i>（<b>断末魔</b>カードを3枚手札から使用するとアップグレード）</i>)
#[LOOT_516][ゴルゴン・ゾーラ]([x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのゴールデンのコピー1体を自分の手札に追加する。)
#[LOOT_521][マスター・オークハート]([x]<b>雄叫び:</b>攻撃力1、2、3のミニオンを1体ずつ<b>招集</b>する。)
#[LOOT_526][クライヤミ]([x]最初は<b>休眠状態</b>。<b>雄叫び:</b>_相手のデッキにロウソク3枚を混ぜる。それらが全て引かれるとこれは目覚める。)
#[LOOT_529][ヴォイド・リッパー](<b>雄叫び:</b>自身を除く全てのミニオンの攻撃力と体力を入れ替える。)
#[LOOT_539][性悪な召喚師]([x]<b>雄叫び:</b>自分のデッキの呪文を1枚表示する。その呪文と同じコストのランダムな____ミニオン1体を召喚する。)
#[LOOT_540][ドラゴン孵化師]([x]自分のターンの終了時ドラゴンを1体<b>招集</b>する。)
#[LOOT_541][キング・トグワグル]([x]<b>雄叫び:</b>相手とデッキを交換する。再度交換するための身代金の呪文1枚を相手に与える。)
#[LOOT_542][大逆の刃キングスベイン](付与された効果を常に維持する。<b>断末魔:</b>この武器を自分のデッキに混ぜる。)
#[NEW1_004][退散]([x]全てのミニオンをそれぞれの所有者の手札に戻す。)
#[NEW1_005][誘拐魔]([x]<b>コンボ:</b> ミニオン1体を___所有者の手札に戻す。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[NEW1_014][変装の達人](<b>雄叫び:</b> 次の自分のターンまで味方のミニオン1体に<b>隠れ身</b>を付与する。)
#[NEW1_016][船長のオウム]([x]<b>雄叫び:</b>自分のデッキのランダムな海賊カード1枚を　自分の手札に追加する。)
#[NEW1_017][飢えたカニ](<b>雄叫び:</b> マーロック1体を破壊し+2/+2を獲得する。)
#[NEW1_018][ブラッドセイルの略奪者]([x]<b>雄叫び:</b> 自分の武器の攻撃力に等しい攻撃力を　追加で獲得する。)
#[NEW1_019][ナイフ・ジャグラー]([x]自分がミニオンを召喚した後ランダムな敵1体に　1ダメージを与える。)
#[NEW1_020][熱狂する火霊術師]([x]自分が呪文を使用した後全てのミニオンに1ダメージを与える。)
#[NEW1_021][終末予言者]([x]自分のターンの開始時全てのミニオンを破壊する。)
#[NEW1_022][悪辣なる海賊]([x]<b>挑発</b>自分の武器の攻撃力1につき_____コストが（1）減る。)
#[NEW1_023][フェアリードラゴン](呪文とヒーローパワーの標的にならない。)
#[NEW1_024][グリーンスキン船長]([x]<b>雄叫び:</b>自分の武器に__+1/+1を付与する。)
#[NEW1_025][ブラッドセイルの海賊]([x]<b>雄叫び:</b> 敵の武器の耐久度を1減らす。)
#[NEW1_026][ヴァイオレット・アイの講師]([x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。)
#[NEW1_027][南海の船長](自身を除く味方の海賊は+1/+1を得る。)
#[NEW1_029][ミルハウス・マナストーム](<b>雄叫び:</b>  次のターン敵の呪文のコストが（0）になる。)
#[NEW1_030][デスウィング]([x]<b>雄叫び:</b> 自身を除く全てのミニオンを破壊し自分の手札を全て破棄する。)
#[NEW1_037][熟練武器職人]([x]自分のターンの終了時自身を除くランダムな味方のミニオン1体に_____攻撃力+1を付与する。_)
#[NEW1_038][グルゥル]([x]各ターンの終了時__+1/+1を獲得する。)
#[NEW1_040][ホガー]([x]自分のターンの終了時<b>挑発</b>を持つ2/2のノールを1体召喚する。)
#[NEW1_041][暴走コドー](<b>雄叫び:</b> 攻撃力2以下の敵のミニオン1体をランダムに破壊する。)
#[OG_034][シリシッド・スウォーマー]([x]このターンに自分のヒーローが攻撃した___場合のみ攻撃できる。)
#[OG_042][放たれし激昂ヤシャラージュ]([x]自分のターンの終了時自分のデッキからミニオン1体を陣地に置く。)
#[OG_070][凶刃の狂信者]([x]<b>コンボ:</b>______+1/+1を獲得する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[OG_072][地の底の探索](<b>断末魔</b>を持つカード1枚を<b>発見</b>する。)
#[OG_073][アザミ茶](カードを1枚引く。さらにそのコピー2枚を自分の手札に追加する。)
#[OG_080][蠱毒なザリル]([x]<b>雄叫び＆断末魔:</b> ランダムな毒素カード1枚を自分の手札に追加する。)
#[OG_082][コボルトの地霊呪痛死](<b>呪文ダメージ+2</b>)
#[OG_102][闇に説くもの](<b>雄叫び:</b> 味方のミニオン1体と攻撃力・体力を入れ替える。)
#[OG_122][峡谷の暴君ムクラ]([x]<b>雄叫び:</b> 「バナナ」2枚を___自分の手札に追加する。)
#[OG_123][変身者ゼラス]([x]このカードが自分の手札にある場合毎ターンこれはランダムなミニオンに変身する。)
#[OG_131][双皇帝ヴェク＝ロア]([x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。)
#[OG_133][頽廃させしものン＝ゾス](<b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。)
#[OG_134][希望の終焉ヨグ＝サロン]([x]<b>雄叫び:</b> この対戦で自分が使用した呪文1回につきランダムな呪文を1つ使用する<i>（対象は_____ランダムに選択される）。_</i>)
#[OG_138][ネルビアンの預言者](自分のターンの開始時このカードのコストを（1）減らす。)
#[OG_141][無貌の巨怪]()
#[OG_142][異界の怪異]()
#[OG_145][マジヤバ・オ・トロン](<b>挑発</b>、<b>聖なる盾</b>)
#[OG_147][狂闘品のヒールロボ]([x]<b>断末魔:</b>敵のヒーローの体力を#8回復する。)
#[OG_150][アマニの凶汚染死]([x]ダメージを受けている間は___攻撃力+2を得る。)
#[OG_151][ン＝ゾスの触手](<b>断末魔:</b> 全てのミニオンに1ダメージを与える。)
#[OG_152][死出路のドラゴンホーク](<b>疾風</b>)
#[OG_153][変・クリーパー](<b>挑発</b>)
#[OG_156][マーロックの鯛ド変態]([x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。)
#[OG_158][熱く教えを乞うもの](<b>断末魔:</b> ランダムな味方のミニオン1体に+1/+1を付与する。)
#[OG_161][コールドライトの妖幻者](<b>雄叫び:</b> マーロックではない全てのミニオンに2ダメージを与える。)
#[OG_162][クトゥーンの門弟](<b>雄叫び:</b> 2ダメージを与える。自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>)
#[OG_173][古のものの血族](自分のターンの終了時味方にこのミニオンが2体いる場合それらは融合して「古のもの」となる。)
#[OG_174][さまよう無貌のもの]([x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。)
#[OG_176][影の一閃](ダメージを受けていないキャラクター1体に$5ダメージを与える。)
#[OG_200][終末予言的中者](自分のターンの開始時このミニオンの攻撃力を7にする。)
#[OG_247][ウォーゲン変異体](<b>隠れ身</b>)
#[OG_248][グマグ・レイジャー]()
#[OG_249][蝕まれしトーレン]([x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。)
#[OG_254][秘密を喰らうもの]([x]<b>雄叫び:</b> 敵の<b>秘策</b>全てを破壊する。破壊した秘策1つにつき+1/+1を獲得する。)
#[OG_255][破滅の招き手](<b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>クトゥーンが死亡している場合クトゥーン1枚を自分のデッキに混ぜる。)
#[OG_256][ン＝ゾスの落とし子]([x]<b>断末魔:</b>味方のミニオン全てに+1/+1を付与する。)
#[OG_267][南海のスキッドフェイス]([x]<b>断末魔:</b> 自分の武器に___攻撃力+2を付与する。)
#[OG_271][鱗の悪夢](自分のターン開始時このミニオンの攻撃力を2倍にする。)
#[OG_272][黄昏の鎚の召喚師](<b>断末魔:</b> 5/5の無貌の破壊者を1体召喚する。)
#[OG_280][クトゥーン]([x]<b>雄叫び:</b>このミニオンの攻撃力に等しい合計ダメージを敵に___ランダムに振り分ける。)
#[OG_281][邪悪の誘い手]([x]<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する<i>___（居場所は問わない）。</i>)
#[OG_282][クトゥーンの刃]([x]<b>雄叫び:</b>ミニオン1体を破壊する。その攻撃力と体力を自分のクトゥーンに追加する<i>（居場所は問わない）。</i>)
#[OG_283][クトゥーンに選ばれし者]([x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>)
#[OG_284][黄昏の鎚の地霊術師]([x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>)
#[OG_286][黄昏の鎚の長老]([x]自分のターンの終了時自分のクトゥーンに+1/+1を付与する___<i>（居場所は問わない）。</i>)
#[OG_290][古代の先遣者](自分のターンの開始時自分のデッキからコスト（10）のミニオン1体を自分の手札に追加する。)
#[OG_291][シャドーキャスター]([x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンの1/1のコピーを自分の手札に追加する。_____そのカードのコストは（1）。_)
#[OG_295][カルトの薬師](<b>雄叫び:</b>敵のミニオン1体につき自分のヒーローの体力を#2回復する。)
#[OG_300][ブギーモンスター]([x]このミニオンの攻撃でミニオンが死亡した時+2/+2を獲得する。)
#[OG_317][竜王デスウィング]([x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。)
#[OG_318][エルウィンの変災ホガー]([x]このミニオンがダメージを受ける度<b>挑発</b>を持つ2/2の　ノールを1体召喚する。)
#[OG_320][ミッドナイト・ドレイク](<b>雄叫び:</b> このカード以外の自分の手札1枚につき攻撃力+1を獲得する。)
#[OG_321][熱狂する信者]([x]<b>挑発:</b> __このミニオンがダメージを受ける度、自分のクトゥーンに+1/+1を付与する<i>（居場所は問わない）。</i>)
#[OG_322][ブラックウォーターの海賊](自分の武器のコストが（2）減少。)
#[OG_323][汚染利品グログロ君](<b>断末魔:</b> カードを1枚引く。)
#[OG_326][石牙の異能死屍]()
#[OG_327][のたうつ触手](<b>挑発</b>)
#[OG_330][アンダーシティの押し売り]([x]<b>断末魔:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。)
#[OG_337][単眼の怪異]([x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。)
#[OG_338][暗黒釣人ナット・ペイグル]([x]相手のターンの開始時相手は50%の確率で___カードを1枚余分に引く。)
#[OG_339][スケラムの狂信者]([x]<b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する___<i>（居場所は問わない）。</i>_)
#[OG_340][這いよるものソゴス](<b>挑発:</b>呪文とヒーローパワーの標的にならない。)
#[PRO_001][エリート・トーレン・チーフテン](<b>雄叫び:</b>  両プレイヤーにロックなパワーあふれるカードを1枚ずつ与える。)
#[SCH_142][貪欲な読書家]([x]自分のターンの終了時手札が3枚になるまでカードを引く。)
#[SCH_143][聖レイジャー](<b>聖なる盾</b>)
#[SCH_145][卓上インプ]()
#[SCH_146][守りのローブ]([x]味方のミニオン全ては「呪文とヒーローパワーの標的にならない」を得る。)
#[SCH_157][魔法の大釜]([x]<b>魔法活性:</b>使われた呪文と同コストのランダムな呪文を使用する。)
#[SCH_160][ワンド職人]([x]<b>雄叫び:</b>自分のクラスのコスト1の呪文1枚を____自分の手札に追加する。)
#[SCH_162][ヴェクタス]([x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。)
#[SCH_182][自然の語り手ギドラ]([x]<b>急襲</b>、<b>疾風</b><b>魔法活性:</b>使われた呪文のコストに等しい攻撃力と体力を獲得する。)
#[SCH_199][転校生]([x]対戦時のゲーム盤に合わせて効果が変化する。)
#[SCH_224][ケルスザード校長](<b>魔法活性:</b>使われた呪文がミニオンを破壊した場合それらのミニオンを召喚する。)
#[SCH_230][オニクスの魔術書士]([x]<b>魔法活性:</b>自分のクラスのランダムな呪文2枚を自分の手札に追加する。)
#[SCH_231][図太い徒弟]([x]<b>魔法活性:</b>攻撃力+2を獲得する。)
#[SCH_232][クリムゾンの竜学生]([x]<b>魔法活性:</b>攻撃力+1と<b>挑発</b>を獲得する。)
#[SCH_234][偽善系の二年生]([x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[SCH_235][退化の矢]([x]コストが（1）低いミニオンに変身させる矢を3本放ち、ランダムな敵のミニオンに振り分ける。)
#[SCH_245][筆記の執精]([x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。)
#[SCH_248][ペン投げ野郎]([x]<b>雄叫び:</b>1ダメージを与える。<b>魔法活性:</b>___これを自分の手札に戻す。)
#[SCH_259][智慧の宝珠]([x]自分のターンの開始時自分のデッキの一番上のカードを見る。耐久度を1失い、それをデッキの一番下に置くことができる。)
#[SCH_270][根源学の予習]([x]<b>呪文ダメージ</b>を持つミニオンを1体<b>発見</b>する。自分が次に使用する<b>呪文ダメージ</b>を持つミニオンのコストが（1）減る。)
#[SCH_273][ラス・フロストウィスパー]([x]自分のターンの終了時全ての敵に$1ダメージを与える<i>（<b>呪文ダメージ</b>によって__強化される）</i>。)
#[SCH_283][マナ食らいのパンサーラ]([x]<b>雄叫び:</b>このターンに自分がヒーローパワーを使っていた場合カードを1枚引く。)
#[SCH_305][秘密の通路](自分の手札を自分のデッキのカード5枚と入れ替える。次のターンに入れ替え前の手札に戻す。)
#[SCH_311][空飛ぶほうき]([x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方のミニオンに<b>急襲</b>を付与する。)
#[SCH_312][ツアーガイド](<b>雄叫び:</b>自分が次に使うヒーローパワーのコストは（0）。)
#[SCH_313][非道の指導教員]([x]<b>魔法活性:</b>自身を除く全てのミニオンに_____2ダメージを与える。__)
#[SCH_350][ワンド泥棒]([x]<b>コンボ:</b>メイジの呪文を1つ<b>発見</b>する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[SCH_351][ジャンディス・バロフ]([x]<b>雄叫び:</b>ランダムなコスト5のミニオン2体を召喚する。2体の内、ダメージを受けると死ぬ1体を秘密裏に選ぶ。)
#[SCH_352][幻影ポーション]([x]味方のミニオン全ての1/1コピーを自分の手札に追加する。それらのコストは（1）。)
#[SCH_425][ドクター・クラスティノフ]([x]<b>急襲</b>このミニオンが攻撃する度自分の武器に+1/+1を付与する。)
#[SCH_426][潜入者リリアン]([x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。)
#[SCH_428][伝承守護者ポルケルト]([x]<b>雄叫び:</b>自分のデッキのカードをコストが高い順に並べ替える。)
#[SCH_509][頭を冷やせ！]([x]ミニオン1体を<b>凍結</b>させる。<b>コンボ:</b>さらに$3ダメージを与える。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[SCH_519][ヴァルペラの毒刃研究者](自分の武器は攻撃力+2を得る。)
#[SCH_521][無理強い]([x]ダメージを受けているミニオン1体を破壊する。<b>コンボ:</b>ミニオン1体を破壊する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[SCH_522][スティールダンサー]([x]<b>雄叫び:</b>自分の武器の攻撃力に等しいコストのランダムなミニオンを1体召喚する。)
#[SCH_530][代理鏡師]([x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。)
#[SCH_537][魔術のトーテム]([x]自分のターンの終了時コスト（3）以下のランダムな呪文を1つ使用する。)
#[SCH_605][湖のスレッシャー]([x]このミニオンは攻撃したミニオンと隣接するミニオンにも____ダメージを与える。)
#[SCH_622][自己研鑽の剣]([x]自分のヒーローが攻撃した後_____攻撃力+1を獲得する。)
#[SCH_623][斧刀講]([x]カードを2枚引く。自分の武器の攻撃力1につきコストが（1）減る。)
#[SCH_706][カンニング]([x]<b>秘策:</b>相手のターンの終了時相手がそのターンに手札から使用した全てのカードのコピーを自分の手札に追加する。)
#[SCH_707][空を翔けるトビウオ]([x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。)
#[SCH_708][日陰草の非行生徒]([x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。)
#[SCH_709][イキってる四年生]([x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。)
#[SCH_710][往餓術師]([x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。)
#[SCH_711][疫病始祖ドレイク]([x]<b>断末魔:</b>ランダムなコスト7のミニオン1体を召喚する。)
#[SCH_713][教団の新入会員]([x]<b>雄叫び:</b>次のターン、相手の呪文のコストが（1）増える。)
#[SCH_714][英才エレク]([x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。)
#[SCH_717][万鍵支配者アラバスター]([x]相手がカードを引く度そのコピー1枚を自分の手札に追加する。____そのコストは（1）。_)
#[TRL_010][ハーフタイムの清掃員]([x]<b>隠れ身</b>、<b>血祭:</b>___装甲を3獲得する。)
#[TRL_015][ダフ屋](<b>血祭:</b>_カードを2枚引く。)
#[TRL_020][盲目のレンジャー]([x]<b>急襲</b>、<b>血祭:</b>1/1の「コウモリ」を2体召喚する。)
#[TRL_057][ヘビの結界](自分のターンの終了時敵のヒーローに2ダメージを与える。)
#[TRL_071][ブラッドセイルの吠猿]([x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方の海賊1体につき+1/+1を獲得する。)
#[TRL_074][ギザギザの歯]([x]<b>断末魔:</b>味方のミニオン全てに<b>急襲</b>を付与する。)
#[TRL_077][グルバシの盛り上げ屋]([x]<b>雄叫び:</b><b>雄叫び</b>を持つミニオンの1/1のコピーを1体<b>発見</b>する。そのミニオンのコストは（1）になる。)
#[TRL_092][サメの精霊]([x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[TRL_096][グリフター](<b>雄叫び:</b>カードを2枚<b>発見</b>する。そのうちランダムな1枚を相手に与える。)
#[TRL_124][ぶんどり部隊](自分のデッキから海賊を2体引く。<b>コンボ:</b>さらに武器を1つ引く。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[TRL_126][フックタスク船長](<b>雄叫び:</b>自分のデッキから海賊を3体召喚し_<b>急襲</b>を付与する。)
#[TRL_127][大砲連射]([x]ランダムな敵1体に$3ダメージを与える。味方の海賊1体につき1回これを繰り返す。)
#[TRL_151][元チャンピオン]([x]<b>雄叫び:</b>5/5の「期待の新人」を1体召喚する。)
#[TRL_156][盗んだナイフ]([x]<i>他のクラスの</i>武器を1つ<b>発見</b>する。)
#[TRL_157][板渡らせの刑]([x]ダメージを受けていないミニオン1体を破壊する。)
#[TRL_312][強仙師](ダメージを受けている間は<b>呪文ダメージ+2</b>を得る。)
#[TRL_363][サロナイト鉱山の奴隷監督]([x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。)
#[TRL_405][野生のビーストマスター]([x]自分が獣を引く度その獣に+2/+2を付与する。)
#[TRL_406][まどろむ狙撃手](ダメージを受けている間は_攻撃力+4を得る。)
#[TRL_407][給水係]([x]<b>雄叫び:</b>このターン中に自分が次に使用するヒーローパワーの_コストを（0）にする。)
#[TRL_409][サメのロア・グラル]([x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。)
#[TRL_503][スカラベの卵]([x]<b>断末魔:</b>1/1の「スカラベ」を3体召喚する。)
#[TRL_504][ブーティ・ベイのノミ屋]([x]<b>雄叫び:</b>相手に「コイン」1枚を与える。)
#[TRL_505][ひ弱なヒナ](<b>断末魔:</b>自分の手札の獣1体のコストを（1）減らす。)
#[TRL_506][グルバシ・チキン](<b>血祭:</b>攻撃力+5を獲得する。)
#[TRL_507][シャークフィンのファン]([x]自分のヒーローが攻撃した後1/1の海賊を1体召喚する。)
#[TRL_508][更生する構成員]([x]自分のターンの開始時このミニオンの体力を#2回復する。)
#[TRL_509][バナナ・バフーン]([x]<b>雄叫び:</b>「バナナ」2枚を___自分の手札に追加する。)
#[TRL_512][小ずるい足噛み魔]([x]<b>生命奪取</b>、<b>雄叫び:</b>__1ダメージを与える。)
#[TRL_513][モッシュオグの審判](<b>挑発</b>、<b>聖なる盾</b>)
#[TRL_514][大虎ノーム]([x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。)
#[TRL_515][会場警備係]([x]<b>挑発</b>敵のミニオン1体につきコストが（1）減る。)
#[TRL_516][グルバシの供物]([x]自分のターンの開始時このミニオンを破壊し装甲を8獲得する。)
#[TRL_517][熱狂的闘技場ファン](<b>雄叫び:</b>自分の手札のミニオン全てに+1/+1を付与する。)
#[TRL_520][マーロック・テイスティーフィン]([x]<b>断末魔:</b>自分のデッキから__マーロックを2体引く。)
#[TRL_521][闘技場の常連客]([x]<b>血祭:</b>「闘技場の常連客」をもう1体召喚する。)
#[TRL_523][ファイアーツリーの呪術医]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____呪文を1つ<b>発見</b>する。)
#[TRL_524][シールドブレイカー](<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。)
#[TRL_525][闘技場の宝箱](<b>断末魔:</b>カードを2枚引く。)
#[TRL_526][ドラゴンモーの爆炎竜]([x]<b>雄叫び:</b>自身を除く全てのミニオンに______1ダメージを与える。)
#[TRL_527][ドラッカリのトリックスター](<b>雄叫び:</b>各プレイヤーは相手のデッキからランダムなカードの__コピーを1枚得る。)
#[TRL_528][前線崩し]([x]<b>血祭:</b>このミニオンの__攻撃力を2倍にする。)
#[TRL_530][覆面選手]([x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合自分のデッキから___<b>秘策</b>を1つ準備する。)
#[TRL_531][ランブルタスク・シェイカー]([x]<b>断末魔:</b>3/2の「ランブルタスク・ブレイカー」を1体召喚する。)
#[TRL_532][モッシュオグのアナウンサー]([x]このミニオンを攻撃する敵は50%の確率で_____別の誰かを攻撃する。)
#[TRL_533][アイスクリーム屋]([x]<b>雄叫び:</b>味方に<b>凍結中</b>のミニオンがいる場合_____装甲を8獲得する。)
#[TRL_535][オオアゴガメのシェルファイター]([x]隣接するミニオンがダメージを受ける度このミニオンが身代わりとなってそのダメージを受ける。)
#[TRL_537][ダ・アンダテイカ]([x]<b>雄叫び:</b>この対戦で死亡した味方のミニオン3体の_____<b>断末魔</b>を獲得する。_)
#[TRL_541][魂剥ぐロア・ハッカー]([x]<b>断末魔:</b>各プレイヤーのデッキに「ケガレた血」を1枚ずつ混ぜる。)
#[TRL_542][ウーンダスタ]([x]<b>急襲</b>、<b>血祭:</b>自分の手札から____獣を1体召喚する。)
#[TRL_546][凶暴なリクガメ]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。)
#[TRL_550][アマニの戦熊](<b>急襲</b>、<b>挑発</b>)

#自分の手札にドラゴンがいる場合
#自分のヒーローの体力を3以上回復する度
#ミニオンが死ぬ度
#自分のデッキに重複するカードがない場合
#自分のターンの終了時
#ダメージを受けている間
#このターンの間
#自分のターンの開始時
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がミニオンを手札から使用する度
#このミニオンを除いて味方に2体以上のミニオンがいる場合

#[UNG_088][トートランの始原術師](<b>雄叫び:</b>呪文1つを<b>発見</b>しランダムな対象に対して使用する。)
#[UNG_089][温厚なメガサウルス]([x]<b>雄叫び:</b>味方のマーロック　全てを<b>適応</b>させる。)
#[UNG_099][電撃デビルサウルス]([x]<b>突撃</b>、<b>雄叫び:</b>このターンの間ヒーローを攻撃できない。)
#[UNG_113][輝く瞳の斥候](<b>雄叫び:</b>カードを1枚引く。そのカードのコストを（5）に変える。)
#[UNG_205][グレイシャル・シャード](<b>雄叫び:</b>敵1体を<b>凍結</b>させる。)
#[UNG_801][巣作りロック鳥]([x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。)
#[UNG_803][エメラルド・リーヴァー](<b>雄叫び:</b>各ヒーローに1ダメージを与える。)
#[UNG_806][ウルトラサウルス]()
#[UNG_807][ゴラッカ・クローラー]([x]<b>雄叫び:</b>海賊1体を破壊し__+1/+1を獲得する。)
#[UNG_808][不屈のカタツムリ]([x]<b>挑発</b>、<b>猛毒</b>)
#[UNG_809][ファイアフライ](<b>雄叫び:</b>1/2のエレメンタル1体を自分の手札に追加する。)
#[UNG_810][ステゴドン](<b>挑発</b>)
#[UNG_812][サーベルストーカー](<b>隠れ身</b>)
#[UNG_813][ストームウォッチャー](<b>疾風</b>)
#[UNG_814][巨大スズメバチ]([x]<b>隠れ身</b>、<b>猛毒</b>)
#[UNG_816][カリモスの下僕]([x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合______エレメンタルを<b>発見</b>する。)
#[UNG_818][即発のエレメンタル](<b>断末魔:</b>ランダムな敵のミニオン1体に　3ダメージを与える。)
#[UNG_823][猛毒の仕込み](自分の武器に<b>猛毒</b>を付与する。)
#[UNG_840][ジャングルハンター・ヒーメット]([x]<b>雄叫び:</b>自分のデッキのコスト（3）以下の____カードを全て破壊する。)
#[UNG_843][ヴォラックス](自分がこのミニオンに呪文を使用した後1/1の植物を1体召喚し呪文のコピーをその植物に対して使用する。)
#[UNG_844][ドデカいレイザーリーフ](攻撃できない。)
#[UNG_845][火成のエレメンタル]([x]<b>断末魔:</b>1/2のエレメンタル2体を自分の手札に追加する。)
#[UNG_847][ブレイズコーラー]([x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合____5ダメージを与える。)
#[UNG_848][始祖ドレイク]([x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。)
#[UNG_851][先遣隊長エリーズ]([x]<b>雄叫び:</b>自分のデッキに未開封の<b>ウンゴロ</b>パック1個を混ぜる。)
#[UNG_856][幻覚]([x]相手のクラスのカードを1枚<b>発見</b>する。)
#[UNG_900][霊の歌い手ウンブラ](自分がミニオンを召喚した後そのミニオンの<b>断末魔</b>を発動する。)
#[UNG_907][オズラック]([x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。)
#[UNG_928][タール・クリーパー]([x]<b>挑発</b>相手のターン中は___攻撃力+2を得る。)
#[UNG_937][原始フィンの見張り番]([x]<b>雄叫び:</b>自分の陣地に他のマーロックがいる場合マーロック1体を<b>発見</b>する。)
#[UNG_946][暴蝕ウーズ](<b>雄叫び:</b>敵の武器を破壊しその攻撃力に等しい装甲を獲得する。)
#[YOD_006][脱走したマナセイバー]([x]<b>隠れ身</b>これが攻撃する度このターンの間のみマナクリスタルを1つ獲得する。)
#[YOD_016][飛掠船員](<b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。)
#[YOD_017][影の彫刻家]([x]<b>コンボ:</b>このターン中に先に使用されたカード1枚につきカードを1枚引く。)
	elif card.name=='BOT_576':
		if condition(game, 'コンボ'):
			return 2

#[YOD_018][蝋術]([x]<b>雄叫び</b>を持つミニオンを1体<b>発見</b>する。そのコストを（2）減らす。)
#[YOD_028][スカイダイビングの教官]([x]<b>雄叫び:</b>自分のデッキからコスト1のミニオンを1体召喚する。)
#[YOD_029][ヘイルブリンガー](<b>雄叫び:</b><b>凍結</b>を持つ1/1の「アイス・シャード」を2体召喚する。)
#[YOD_030][認可冒険者]([x]<b>雄叫び:</b>自分が<b>クエスト</b>中の場合自分の手札に「コイン」1枚を追加する。)
#[YOD_032][飢える陰獣フェルウィング](このターン中に相手に与えたダメージ1につき__コストが（1）減る。)
#[YOD_033][ブームピストル無頼]([x]<b>雄叫び:</b>次のターン敵の<b>雄叫び</b>を持つカードの__コストが（5）増える。)
#[YOD_035][悪の大手先アーク]([x]自分が<b>悪の手先</b>を手札から使用した後<b>悪の手先</b>1枚を自分の___手札に追加する。)
#[YOD_038][空賊大将クラッグ]([x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。)
