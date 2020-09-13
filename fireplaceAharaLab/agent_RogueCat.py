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
		if '沈黙' in dscrpt:
			print("		elif ID  == '%s':"%(card.id))
			print("			cond1.append(['silence','', ''])")
			print("			#%s : %s"%(card.name, card.description.replace('\n','')))
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
	if  card.charge:
		if ID == 'AT_070':
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
	if card.has_deathrattle:
		#断末魔　死ぬときに発動 deathrattle
		#発動のタイミングが相手に依存しているの、基本的にいつでも。
		#内容によっては場との関連がありうる。
		#ミニオンを召喚したりカードを追加したり相手にダメージを与えるものはいつでもOK
		#相手ミニオンに力があり、出してもすぐに殺されることがわかっているときは優先。
		#全体にダメージを与えるもの、自分にダメージを与えるものには注意。
		if 'AT_' in ID:
			if ID == 'AT_036':
				cond1.append(['deathrattle','', 'summon'])
				#アヌバラク : [x]<b>断末魔:</b>このカードを自分の手札に戻し4/4のネルビアン1体を[x]召喚する。
			elif ID == 'AT_123':
				cond1.append(['deathrattle','haveDragon(game)', 'damageAll'])
				#チルモー : [x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。
			elif ID == 'AT_128':
				cond1.append(['deathrattle','', 'backCardHand'])
				#骸骨騎士 : [x]<b>断末魔:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、このミニオンを自分の手札に戻す。
		elif 'BOT_' in ID:
			if ID == 'BOT_031':
				cond1.append(['deathrattle','', 'damage'])
				#ゴブリン爆弾 : [x]<b>断末魔:</b>敵のヒーローに___2ダメージを与える。
			elif ID == 'BOT_066':
				cond1.append(['deathrattle','', 'summon'])
				#メカ・チビドラゴン : [x]<b>断末魔:</b>7/7の「メカ・ドラゴン」を__1体召喚する。
			elif ID == 'BOT_084':
				cond1.append(['deathrattle','', 'addCardHand'])
				#紫の煙霧 : [x]<b>断末魔</b>を持つランダムなカード2枚を自分の手札に追加する。
			elif ID == 'BOT_102':
				cond1.append(['deathrattle','', 'addCardHand'])
				#スパーク・ドリル : [x]<b>急襲</b><b>断末魔:</b><b>急襲</b>を持つ1/1の「スパーク」2体を自分の手札に追加する。
			elif ID == 'BOT_267':
				cond1.append(['deathrattle','', 'summon'])
				#手動操縦のリーパー : [x]<b>断末魔:</b>自分の手札からコスト（2）以下のランダムなミニオンを1体召喚する。
			elif ID == 'BOT_286':
				cond1.append(['deathrattle','', 'help'])
				#ネクリウムの刃 : [x]<b>断末魔:</b>ランダムな味方のミニオン1体の____<b>断末魔</b>を発動する。
			elif ID == 'BOT_312':
				cond1.append(['deathrattle','', 'summon'])
				#自己増殖型メナス : [x]<b>超電磁</b><b>断末魔:</b>1/1の「マイクロロボ」を3体召喚する。
			elif ID == 'BOT_401':
				cond1.append(['deathrattle','', 'addCardHand'])
				#兵器化ピニャータ : [x]<b>断末魔:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の_____手札に追加する。
			elif ID == 'BOT_424':
				cond1.append(['deathrattle','noDeck(game) and noHand(game) and noCharacter(game)', 'damageHero'])
				#メックトゥーン : [x]<b>断末魔:</b>自分のデッキ、手札、陣地にカードがない場合_____敵のヒーローを破壊する。
			elif ID == 'BOT_445':
				cond1.append(['deathrattle','', 'summon'])
				#メカンガルー : [x]<b>断末魔:</b>1/1の「コメカンガルー」を1体召喚する。
			elif ID == 'BOT_508':
				cond1.append(['deathrattle','', 'help'])
				#ネクリウムの小瓶 : [x]味方のミニオン1体の<b>断末魔</b>を___2回発動させる。
			elif ID == 'BOT_565':
				cond1.append(['deathrattle','', 'summon'])
				#ブライトノズル・クローラー : <b>断末魔:</b><b>猛毒</b>と<b>急襲</b>を持つ1/1のウーズを1体召喚する。
			elif ID == 'BOT_606':
				cond1.append(['deathrattle','heHasMinion(game)', 'damage'])
				#ブーマーロボ : <b>断末魔:</b>ランダムな敵のミニオン1体に__4ダメージを与える。
			elif ID == 'BOT_700':
				cond1.append(['deathrattle','', 'summon'])
				#チョッキンガー : <b>超電磁</b>、<b>木霊</b><b>断末魔:</b>1/1の「マイクロロボ」を2体召喚する。
		elif ID == 'BRM_027':
			cond1.append(['deathrattle','', 'changeHero'])
			#筆頭家老エグゼクタス : [x]<b>断末魔:</b>自分のヒーローを「炎の王ラグナロス」と置き換える。
		elif 'BT_' in ID:
			if ID == 'BT_008':
				cond1.append(['deathrattle','', 'summon'])
				#錆鉄の入門者 : [x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。
			elif ID == 'BT_126':
				cond1.append(['deathrattle','', 'summon'])
				#テロン・ゴアフィーンド : [x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。
			elif ID == 'BT_155':
				cond1.append(['deathrattle','', 'summon'])
				#屑鉄山のコロッサス : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。
			elif ID == 'BT_160':
				cond1.append(['deathrattle','', 'help'])
				#錆鉄の狂信者 : [x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。
			elif ID == 'BT_703':
				cond1.append(['deathrattle','', 'summon'])
				#呪われた流れ者 : [x]<b>断末魔:</b><b>隠れ身</b>を持つ7/5の影を1体召喚する。
			elif ID == 'BT_713':
				cond1.append(['deathrattle','', 'addCardDeck'])
				#アカマ : [x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。
			elif ID == 'BT_726':
				cond1.append(['deathrattle','', 'summon'])
				#ドラゴンモーの飛行追跡者 : <b>断末魔:</b>3/4の「ドラゴンライダー」を1体召喚する。
			elif ID == 'BT_728':
				cond1.append(['deathrattle','', 'summon'])
				#顔を隠した放浪者 : <b>断末魔:</b>9/1の審問官を1体召喚する。
			elif ID == 'BT_735':
				cond1.append(['deathrattle','', 'summon'])
				#アラール : [x]<b>断末魔</b>:0/3の「アラールの灰」を1体召喚する。次の自分のターンに灰は___「アラール」に変身する。
		elif 'CFM_' in ID:
			if ID == 'CFM_095':
				cond1.append(['deathrattle','', 'addCardHisDeck'])
				#穴掘りイタチ : [x]<b>断末魔:</b> このミニオンを相手のデッキに混ぜる。
			elif ID == 'CFM_120':
				cond1.append(['deathrattle','', 'restoreBoth'])
				#超うざい調剤師 : [x]<b>断末魔:</b>各ヒーローの体力を#4回復する。
			elif ID == 'CFM_341':
				cond1.append(['deathrattle','heHasMinion(game)', 'damage'])
				#サリー巡査部長 : <b>断末魔:</b>敵のミニオン全てにこのミニオンの攻撃力に等しいダメージを与える。
			elif ID == 'CFM_646':
				cond1.append(['deathrattle','', 'damage'])
				#裏町のレプラノーム : [x]<b>断末魔:</b>敵のヒーローに____2ダメージを与える。
			elif ID == 'CFM_667':
				cond1.append(['deathrattle','heHasMinion(game)', 'damage'])
				cond1.append(['deathrattle','', 'damageSelf'])
				#爆弾部隊 : [x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。
			elif ID == 'CFM_691':
				cond1.append(['deathrattle','', 'summon'])
				#翡翠の鎌刀 : [x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
			elif ID == 'CFM_902':
				cond1.append(['deathrattle','', 'summon'])
				#アヤ・ブラックポー : [x]<b>雄叫び＆断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び＆断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
		elif 'DAL_' in ID:
			if ID == 'DAL_088':
				cond1.append(['deathrattle','', 'summon'])
				#金庫番 : <b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。
			elif ID == 'DAL_566':
				cond1.append(['deathrattle','', 'summon'])
				#奇抜な書記官 : [x]<b>断末魔:</b>1/1の「息巻く巻物」を4体召喚する。
			elif ID == 'DAL_720':
				cond1.append(['deathrattle','', 'backCardHand'])
				#ワグル・ピック : [x]<b>断末魔:</b>ランダムな味方のミニオン1体を自分の手札に戻す。そのミニオンのコストは（2）減る。
			elif ID == 'DAL_743':
				cond1.append(['deathrattle','', 'summon'])
				#ヘンチ・クランの騎豚 : [x]<b>急襲</b>、<b>断末魔:</b>1/1のマーロックを1体召喚する。
			elif ID == 'DAL_749':
				cond1.append(['deathrattle','card.atk>=4', 'summon'])
				#神出鬼没の怪人 : [x]<b>断末魔:</b>このミニオンの攻撃力が4以上の場合__再度召喚する。
			elif ID == 'DAL_775':
				cond1.append(['deathrattle','', 'damageAll'])
				#トンネル爆破係 : [x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。
		elif 'DRG_' in ID:
			if ID == 'DRG_036':
				cond1.append(['deathrattle','', 'summon'])
				#ワクサドレッド : [x]<b>断末魔:</b>引かれた際「ワクサドレッド」を再度召喚するロウソク1枚を______自分のデッキに混ぜる。_
			elif ID == 'DRG_049':
				cond1.append(['deathrattle','haveDragon(game)', 'help'])
				#美味しいマロバルーン : <b>断末魔:</b>自分の手札のドラゴン1体に__+2/+2を付与する。
			elif ID == 'DRG_071':
				cond1.append(['deathrattle','', 'addSmallCardHisDeck'])
				#悪運アホウドリ : [x]<b>断末魔:</b>相手のデッキに1/1の「アホウドリ」2体を混ぜる。
			elif ID == 'DRG_086':
				cond1.append(['deathrattle','', 'drawCard'])
				#クロマティックの卵 : [x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！
		elif 'EX1_' in ID:
			if ID == 'EX1_012':
				cond1.append(['deathrattle','', 'drawCard'])
				#ブラッドメイジ・サルノス : [x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。
			elif ID == 'EX1_016':
				cond1.append(['deathrattle','', 'getMinion'])
				#シルヴァナス・ウィンドランナー : [x]<b>断末魔:</b>ランダムな敵のミニオン1体を味方にする。
			elif ID == 'EX1_029':
				cond1.append(['deathrattle','', 'damage'])
				#レプラノーム : [x]<b>断末魔:</b> 敵のヒーローに　2ダメージを与える。
			elif ID == 'EX1_096':
				cond1.append(['deathrattle','', 'drawCard'])
				#戦利品クレクレ君 : [x]<b>断末魔:</b>カードを1枚引く。
			elif ID == 'EX1_097':
				cond1.append(['deathrattle','', 'damageAll'])
				#涜れしもの : [x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。
			elif ID == 'EX1_110':
				cond1.append(['deathrattle','', 'summon'])
				#ケーアン・ブラッドフーフ : [x]<b>断末魔:</b>4/5のベイン・ブラッドフーフを1体召喚する。
			elif ID == 'EX1_556':
				cond1.append(['deathrattle','', 'summon'])
				#刈入れゴーレム : [x]<b>断末魔:</b> 2/1の壊れかけのゴーレムを1体召喚する。
			elif ID == 'EX1_577':
				cond1.append(['deathrattle','', 'summonHisMion'])
				#魔獣 : [x]<b>断末魔:</b> 3/3のフィンクル・アインホルンを1体敵の陣地に召喚する。
		elif 'FP1_' in ID:
			if ID == 'FP1_001':
				cond1.append(['deathrattle','myHeroMaxHealth>myHeroHealth', 'restore'])
				#エサゾンビ : [x]<b>断末魔:</b>敵のヒーローの体力を#5回復する。
			elif ID == 'FP1_002':
				cond1.append(['deathrattle','', 'summon'])
				#呪われた蜘蛛 : <b>断末魔:</b> 1/1の亡霊蜘蛛を2体召喚する。
			elif ID == 'FP1_004':
				cond1.append(['deathrattle','', 'addCardDeck'])
				#マッドサイエンティスト : [x]<b>断末魔:</b> 自分のデッキにある_______<b>秘策</b>1枚を準備する。
			elif ID == 'FP1_007':
				cond1.append(['deathrattle','', 'summon'])
				#ネルビアンの卵 : <b>断末魔:</b> 4/4のネルビアンを1体召喚する。
			elif ID == 'FP1_009':
				cond1.append(['deathrattle','', 'summonHisMinion'])
				#デスロード : [x]<b>挑発、断末魔:</b> 相手プレイヤーはデッキからミニオン_______1体を陣地に置く。_
			elif ID == 'FP1_012':
				cond1.append(['deathrattle','', 'summon'])
				#ヘドロゲッパー : [x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。
			elif ID == 'FP1_014':
				cond1.append(['deathrattle','', 'summon'])
				#スタラグ : <b>断末魔:</b> この対戦中にフューゲンも死亡した場合、サディアスを召喚する。
			elif ID == 'FP1_015':
				cond1.append(['deathrattle','', 'summon'])
				#フューゲン : [x]<b>断末魔:</b> この対戦中にスタラグも死亡していた場合____サディアスを召喚する。
			elif ID == 'FP1_024':
				cond1.append(['deathrattle','', 'damageAll'])
				#不安定なグール : [x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。
			elif ID == 'FP1_026':
				cond1.append(['deathrattle','', 'backCardHand'])
				#アヌバー・アンブッシャー : [x]<b>断末魔:</b> ランダムな味方のミニオン1体を_______自分の手札に戻す。_
			elif ID == 'FP1_029':
				cond1.append(['deathrattle','', 'drawCard'])
				#踊る剣 : [x]<b>断末魔:</b>相手はカードを1枚引く。
			elif ID == 'FP1_031':
				cond1.append(['','haveDeathrattleMinion(game)', ''])
				#バロン・リーヴェンデア : [x]味方のミニオンの__<b>断末魔</b>は2回発動する。
		elif 'GIL_' in ID:
			if ID == 'GIL_118':
				cond1.append(['deathrattle','', 'restore'])
				#キジル博士 : [x]<b>断末魔:</b>自分のヒーローの体力を#8回復する。
			elif ID == 'GIL_513':
				cond1.append(['deathrattle','', 'help'])
				#迷える魂 : <b>断末魔:</b>味方のミニオン全てに攻撃力+1を__付与する。
			elif ID == 'GIL_557':
				cond1.append(['deathrattle','', 'drawCard'])
				#呪われた漂流者 : [x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。
			elif ID == 'GIL_614':
				cond1.append(['deathrattle','', 'damage'])
				#ヴードゥー人形 : [x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。
			elif ID == 'GIL_616':
				cond1.append(['deathrattle','', 'summon'])
				#裂けるフェスタールート : [x]<b>断末魔:</b>2/2の「裂けた若木」を2体召喚する。
			elif ID == 'GIL_667':
				cond1.append(['deathrattle','', 'restore'])
				#朽ちかけたアップルバウム : [x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。
			elif ID == 'GIL_816':
				cond1.append(['deathrattle','', 'drawCard'])
				#沼のドラゴンの卵 : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
		elif 'GVG_' in ID:
			if ID == 'GVG_076':
				cond1.append(['deathrattle','', 'damageAll'])
				#爆発ヒツジ : <b>断末魔:</b> 全てのミニオンに2ダメージを与える。
			elif ID == 'GVG_078':
				cond1.append(['deathrattle','', 'drawCard'])
				#メカ・イェティ : <b>断末魔:</b> 各プレイヤーに<b>スペアパーツ</b>カード1枚を与える。
			elif ID == 'GVG_082':
				cond1.append(['deathrattle','', 'drawCard'])
				#ゼンマイ仕掛けのノーム : <b>断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
			elif ID == 'GVG_096':
				cond1.append(['deathrattle','', 'summon'])
				#手動操縦のシュレッダー : <b>断末魔:</b> ランダムなコスト2のミニオン1体を召喚する。
			elif ID == 'GVG_097':
				cond1.append(['deathrattle','heHasMinion(game)', 'help'])
				#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
			elif ID == 'GVG_105':
				cond1.append(['deathrattle','', 'summon'])
				#手動操縦のスカイ・ゴーレム : <b>断末魔:</b> ランダムなコスト4のミニオン1体を召喚する。
			elif ID == 'GVG_114':
				cond1.append(['deathrattle','', 'summon'])
				#スニードの旧型シュレッダー : <b>断末魔:</b> ランダムな<b>レジェンド</b>のミニオン1体を召喚する。
			elif ID == 'GVG_115':
				cond1.append(['deathrattle','', 'drawCard'])
				#トッシュリー : [x]<b>雄叫び、断末魔:</b> <b>スペアパーツ</b>カード1枚を自分の手札に追加する。
		elif 'ICC_' in ID:
			if ID == 'ICC_019':
				cond1.append(['deathrattle','', 'summon'])
				#骸骨術師 : [x]<b>断末魔:</b>今が相手のターンの場合8/8のスケルトンを1体召喚する。
			elif ID == 'ICC_025':
				cond1.append(['deathrattle','', 'summon'])
				cond1.append(['deathrattle','', 'summonHisMinion'])
				#ガラガラガイコツ : [x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。
			elif ID == 'ICC_027':
				cond1.append(['deathrattle','', 'drawCard'])
				#ボーン・ドレイク : [x]<b>断末魔:</b>ランダムなドラゴン1体を自分の手札に追加する。
			elif ID == 'ICC_065':
				cond1.append(['deathrattle','', 'drawCard'])
				#ボーン・バロン : <b>断末魔:</b>1/1のスケルトン2体を自分の手札に追加する。
			elif ID == 'ICC_067':
				cond1.append(['deathrattle','', 'summon'])
				#ヴライグール : [x]<b>断末魔:</b>今が相手のターンの場合2/2のグールを1体召喚する。
			elif ID == 'ICC_098':
				cond1.append(['deathrattle','', 'drawCard'])
				#墓に潜むもの : [x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。
			elif ID == 'ICC_099':
				cond1.append(['deathrattle','', 'damageSelf'])
				#涜れし爆弾 : <b>断末魔:</b>味方のミニオン全てに5ダメージを与える。
			elif ID == 'ICC_201':
				cond1.append(['deathrattle','', 'drawCard'])
				#骰は投げられた : [x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。
			elif ID == 'ICC_702':
				cond1.append(['deathrattle','', 'drawCard'])
				#浅めの墓穴堀り : <b>断末魔:</b><b>断末魔</b>を持つランダムなミニオン1体を自分の手札に追加する。
			elif ID == 'ICC_812':
				cond1.append(['deathrattle','', 'summon'])
				#ミートワゴン : [x]<b>断末魔:</b>このミニオンより攻撃力が低いミニオンを1体自分のデッキから召喚する。
			elif ID == 'ICC_854':
				cond1.append(['deathrattle','', 'drawCard'])
				#アーファス : <b>断末魔:</b>ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。
		elif 'KAR_' in ID:
			if ID == 'KAR_029':
				cond1.append(['deathrattle','', 'drawCard'])
				#ルーンの卵 : <b>断末魔:</b>カードを1枚引く。
			elif ID == 'KAR_041':
				cond1.append(['deathrattle','', 'summon'])
				#堀に潜むもの : <b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。
			elif ID == 'KAR_094':
				cond1.append(['deathrattle','', 'drawCard'])
				#殺意のフォーク : <b>断末魔:</b>3/2の武器1枚を自分の手札に追加する。
		elif 'LOE_' in ID:
			if ID == 'LOE_012':
				cond1.append(['deathrattle','', 'drawCard'])
				#墓荒らし : <b>断末魔:</b> 自分の手札に「コイン」1枚を追加する。
			elif ID == 'LOE_046':
				cond1.append(['deathrattle','', 'damage'])
				#巨大ガマ : <b>断末魔:</b> ランダムな敵1体に1ダメージを与える。
			elif ID == 'LOE_061':
				cond1.append(['deathrattle','haveMinion(game)', 'help'])
				#アヌビサス・センチネル : [x]<b>断末魔:</b>ランダムな味方のミニオン1体に____+3/+3を付与する。
			elif ID == 'LOE_089':
				cond1.append(['deathrattle','', 'summon'])
				#ふらつくこびと達 : <b>断末魔:</b> 2/2のこびとを3体召喚する。
		elif 'LOOT_' in ID:
			if ID == 'LOOT_144':
				cond1.append(['deathrattle','', 'addCardHisHand'])
				#護宝のドラゴン : [x]<b>断末魔:</b>相手に「コイン」2枚を与える。
			elif ID == 'LOOT_153':
				cond1.append(['deathrattle','', 'summon'])
				#ヴァイオレット・ヴルム : <b>断末魔:</b>1/1の「芋虫」を7体召喚する。
			elif ID == 'LOOT_161':
				cond1.append(['deathrattle','', 'summon'])
				#肉食キューブ : [x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。
			elif ID == 'LOOT_184':
				cond1.append(['deathrattle','', 'summon'])
				#シルバーヴァンガード : [x]<b>断末魔:</b>コスト8のミニオンを1体<b>招集</b>する。
			elif ID == 'LOOT_233':
				cond1.append(['deathrattle','', 'summon'])
				#呪われた門弟 : [x]<b>断末魔:</b>5/1のレヴナントを1体召喚する。
			elif ID == 'LOOT_412':
				cond1.append(['deathrattle','haveMinion(game)', 'summon'])
				#コボルトの幻術師 : [x]<b>断末魔:</b>自分の手札からミニオン1体の1/1のコピーを1体召喚する。
			elif ID == 'LOOT_413':
				cond1.append(['deathrattle','', 'help'])
				#装甲虫 : <b>断末魔:</b>装甲を3獲得する。
			elif ID == 'LOOT_542':
				cond1.append(['deathrattle','', 'addCardDeck'])
				#大逆の刃キングスベイン : 付与された効果を常に維持する。<b>断末魔:</b>この武器を自分のデッキに混ぜる。
		elif 'OG_' in ID:
			if ID == 'OG_072':
				cond1.append(['drawCard','', 'deathrattle'])
				#地の底の探索 : <b>断末魔</b>を持つカード1枚を<b>発見</b>する。
			elif ID == 'OG_080':
				cond1.append(['deathrattle','', 'drawCard'])
				#蠱毒なザリル : [x]<b>雄叫び＆断末魔:</b> ランダムな毒素カード1枚を自分の手札に追加する。
			elif ID == 'OG_133':
				cond1.append(['deathrattle','', 'summon'])
				#頽廃させしものン＝ゾス : <b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。
			elif ID == 'OG_147':
				cond1.append(['deathrattle','', 'restore'])
				#狂闘品のヒールロボ : [x]<b>断末魔:</b>敵のヒーローの体力を#8回復する。
			elif ID == 'OG_151':
				cond1.append(['deathrattle','', 'damageAll'])
				#ン＝ゾスの触手 : <b>断末魔:</b> 全てのミニオンに1ダメージを与える。
			elif ID == 'OG_158':
				cond1.append(['deathrattle','', 'help'])
				#熱く教えを乞うもの : <b>断末魔:</b> ランダムな味方のミニオン1体に+1/+1を付与する。
			elif ID == 'OG_249':
				cond1.append(['deathrattle','', 'summon'])
				#蝕まれしトーレン : [x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。
			elif ID == 'OG_256':
				cond1.append(['deathrattle','', 'help'])
				#ン＝ゾスの落とし子 : [x]<b>断末魔:</b>味方のミニオン全てに+1/+1を付与する。
			elif ID == 'OG_267':
				cond1.append(['deathrattle','', 'help'])
				#南海のスキッドフェイス : [x]<b>断末魔:</b> 自分の武器に___攻撃力+2を付与する。
			elif ID == 'OG_272':
				cond1.append(['deathrattle','', 'summon'])
				#黄昏の鎚の召喚師 : <b>断末魔:</b> 5/5の無貌の破壊者を1体召喚する。
			elif ID == 'OG_317':
				cond1.append(['deathrattle','haveDragon(game)', 'playCard'])
				#竜王デスウィング : [x]<b>断末魔:</b>自分の手札のドラゴンを全て戦場に出す。
			elif ID == 'OG_323':
				cond1.append(['deathrattle','', 'drawCard'])
				#汚染利品グログロ君 : <b>断末魔:</b> カードを1枚引く。
			elif ID == 'OG_330':
				cond1.append(['deathrattle','', 'drawCard'])
				#アンダーシティの押し売り : [x]<b>断末魔:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
		elif 'SCH_' in ID:
			if ID == 'SCH_162':
				cond1.append(['deathrattle','', 'summon'])
				#ヴェクタス : [x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。
			elif ID == 'SCH_426':
				cond1.append(['deathrattle','', 'summon'])
				#潜入者リリアン : [x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。
			elif ID == 'SCH_707':
				cond1.append(['deathrattle','', 'drawCard'])
				#空を翔けるトビウオ : [x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。
			elif ID == 'SCH_708':
				cond1.append(['deathrattle','', 'drawCard'])
				#日陰草の非行生徒 : [x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。
			elif ID == 'SCH_709':
				cond1.append(['deathrattle','', 'drawCard'])
				#イキってる四年生 : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。
			elif ID == 'SCH_711':
				cond1.append(['deathrattle','', 'summon'])
				#疫病始祖ドレイク : [x]<b>断末魔:</b>ランダムなコスト7のミニオン1体を召喚する。
			elif ID == 'SCH_714':
				cond1.append(['deathrattle','', 'addCardDeck'])
				#英才エレク : [x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
		elif 'TRL_' in ID:
			if ID == 'TRL_074':
				cond1.append(['deathrattle','', 'help'])
				#ギザギザの歯 : [x]<b>断末魔:</b>味方のミニオン全てに<b>急襲</b>を付与する。
			elif ID == 'TRL_363':
				cond1.append(['deathrattle','', 'summonHisMinion'])
				#サロナイト鉱山の奴隷監督 : [x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。
			elif ID == 'TRL_409':
				cond1.append(['deathrattle','', 'drawCard'])
				#サメのロア・グラル : [x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。
			elif ID == 'TRL_503':
				cond1.append(['deathrattle','', 'summon'])
				#スカラベの卵 : [x]<b>断末魔:</b>1/1の「スカラベ」を3体召喚する。
			elif ID == 'TRL_505':
				cond1.append(['deathrattle','haveBeast(game)', 'help'])
				#ひ弱なヒナ : <b>断末魔:</b>自分の手札の獣1体のコストを（1）減らす。
			elif ID == 'TRL_520':
				cond1.append(['deathrattle','', 'drawCard'])
				#マーロック・テイスティーフィン : [x]<b>断末魔:</b>自分のデッキから__マーロックを2体引く。
			elif ID == 'TRL_525':
				cond1.append(['deathrattle','', 'drawCard'])
				#闘技場の宝箱 : <b>断末魔:</b>カードを2枚引く。
			elif ID == 'TRL_531':
				cond1.append(['deathrattle','', 'summon'])
				#ランブルタスク・シェイカー : [x]<b>断末魔:</b>3/2の「ランブルタスク・ブレイカー」を1体召喚する。
			elif ID == 'TRL_541':
				cond1.append(['deathrattle','', 'addCardDeck'])
				#魂剥ぐロア・ハッカー : [x]<b>断末魔:</b>各プレイヤーのデッキに「ケガレた血」を1枚ずつ混ぜる。
		elif 'ULD_' in ID:
			if ID == 'ULD_174':
				cond1.append(['deathrattle','', 'summon'])
				#ヘビの卵 : <b>断末魔:</b>3/4の「シーサーペント」を1体召喚する。
			elif ID == 'ULD_177':
				cond1.append(['deathrattle','', 'drawCard'])
				#オクトサリ : <b>断末魔:</b>カードを8枚引く。
			elif ID == 'ULD_183':
				cond1.append(['deathrattle','haveMinion(game)', 'help'])
				#アヌビサス・ウォーブリンガー : <b>断末魔:</b>自分の手札のミニオン全てに+3/+3を付与する。
			elif ID == 'ULD_184':
				cond1.append(['deathrattle','', 'damage'])
				#コボルトのサンドトルーパー : [x]<b>断末魔:</b>敵のヒーローに___3ダメージを与える。
			elif ID == 'ULD_208':
				cond1.append(['deathrattle','', 'restore'])
				#カルトゥートの守護者 : [x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。
			elif ID == 'ULD_250':
				cond1.append(['deathrattle','', 'drawCard'])
				#虫食いゴブリン : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。
			elif ID == 'ULD_280':
				cond1.append(['deathrattle','heHasMinion(game)', 'backCardHisHand'])
				#サーケットの昏倒強盗 : <b>断末魔:</b>ランダムな敵のミニオン1体を___相手の手札に戻す。
			elif ID == 'ULD_282':
				cond1.append(['deathrattle','', 'DrawCard'])
				#壺の商人 : [x]<b>断末魔:</b>ランダムなコスト1のミニオン1体を____自分の手札に追加する。
			elif ID == 'ULD_706':
				cond1.append(['deathrattle','', 'summon'])
				#バレバレの囮 : [x]<b>断末魔:</b>各プレイヤーは手札の最もコストが低いミニオンを1体召喚する。
		elif 'UNG_' in ID:
			if ID == 'UNG_010':
				cond1.append(['deathrattle','', 'summon'])
				#満腹のスレッシャドン : [x]<b>断末魔:</b>1/1のマーロックを3体召喚する。
			elif ID == 'UNG_065':
				cond1.append(['deathrattle','', 'asleep'])
				#死体花シェラジン : [x]<b>断末魔:</b><b>休眠状態</b>になる。1ターン中に4枚のカードを手札から使用すると______このミニオンは復活する。_
			elif ID == 'UNG_076':
				cond1.append(['deathrattle','', 'summon'])
				#卵泥棒 : [x]<b>断末魔:</b>1/1のラプターを2体召喚する。
			elif ID == 'UNG_083':
				cond1.append(['deathrattle','', 'summon'])
				#デビルサウルスの卵 : [x]<b>断末魔:</b>5/5のデビルサウルスを1体召喚する。
			elif ID == 'UNG_818':
				cond1.append(['deathrattle','heHasMinion(game)', 'damage'])
				#即発のエレメンタル : <b>断末魔:</b>ランダムな敵のミニオン1体に　3ダメージを与える。
			elif ID == 'UNG_845':
				cond1.append(['deathrattle','', 'drawCard'])
				#火成のエレメンタル : [x]<b>断末魔:</b>1/2のエレメンタル2体を自分の手札に追加する。
			elif ID == 'UNG_900':
				cond1.append(['deathrattle','', 'help'])
				#霊の歌い手ウンブラ : 自分がミニオンを召喚した後そのミニオンの<b>断末魔</b>を発動する。
		elif 'YOD_' in ID:
			if ID == 'YOD_016':
				cond1.append(['deathrattle','', 'drawCard'])
				#飛掠船員 : <b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。
	if card.has_battlecry:#雄叫び。場に出たときに発動 battlecry
		#基本的にいつでも。内容によっては場との関連がありうる。
		#内容の精査が必要
		if 'AT_' in ID:
			if ID == 'AT_017':
				cond1.append(['battlecry','haveDragon(game)', ''])
				#トワイライトの守護者 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。
			elif ID == 'AT_032':
				cond1.append(['battlecry','havePirate(game) or onPirate(game)', ''])
				#闇商人 : [x]<b>雄叫び:</b>味方に海賊がいる場合___+1/+1を獲得する。
			elif ID == 'AT_084':
				cond1.append(['battlecry','haveMinion(game)', ''])
				#槍持ち : <b>雄叫び:</b> 味方のミニオン1体に攻撃力+2を付与する。
			elif ID == 'AT_086':
				cond1.append(['battlecry','', ''])
				#妨害工作員 : [x]<b>雄叫び:</b> 次のターン、相手のヒーローパワーの____コストが（5）増える。
			elif ID == 'AT_094':
				cond1.append(['battlecry','', ''])
				#火炎ジャグラー : <b>雄叫び:</b>ランダムな敵1体に1ダメージを与える。
			elif ID == 'AT_096':
				cond1.append(['battlecry','', ''])
				#ゼンマイ仕掛けの騎士 : [x]<b>雄叫び:</b> 味方のメカ1体に__+1/+1を付与する。
			elif ID == 'AT_098':
				cond1.append(['battlecry','', ''])
				#大道芸の呪文喰い : [x]<b>雄叫び:</b>相手のヒーローパワーをコピーする。
			elif ID == 'AT_103':
				cond1.append(['battlecry','', ''])
				#北海のクラーケン : <b>雄叫び:</b> 4ダメージを与える。
			elif ID == 'AT_105':
				cond1.append(['battlecry','', ''])
				#傷を負ったクヴァルディル : <b>雄叫び:</b> このミニオンに3ダメージを与える。
			elif ID == 'AT_106':
				cond1.append(['battlecry','heHasDevil(game)', 'silence'])
				#光の勇者 : <b>雄叫び:</b> 悪魔1体を<b>沈黙</b>させる。
			elif ID == 'AT_108':
				cond1.append(['battlecry','', ''])
				#重装戦馬 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>突撃</b>を獲得する。
			elif ID == 'AT_111':
				cond1.append(['battlecry','', ''])
				#スナック売り : <b>雄叫び:</b>各ヒーローの体力を#4回復する。
			elif ID == 'AT_112':
				cond1.append(['battlecry','', ''])
				#槍試合の名手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。
			elif ID == 'AT_115':
				cond1.append(['battlecry','', ''])
				#フェンシングのコーチ : <b>雄叫び:</b> [x]次に自分のヒーローパワーを使う時、そのコストが（2）減る。
			elif ID == 'AT_117':
				cond1.append(['battlecry','', ''])
				#司会者 : <b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。
			elif ID == 'AT_118':
				cond1.append(['battlecry','', ''])
				#グランド・クルセイダー : <b>雄叫び:</b> ランダムなパラディン用カード1枚を自分の手札に追加する。
			elif ID == 'AT_122':
				cond1.append(['battlecry','', ''])
				#串刺しのゴーモック : <b>雄叫び:</b> このミニオンを除いて味方に4体以上ミニオンがいる場合4ダメージを与える。
			elif ID == 'AT_132':
				cond1.append(['battlecry','', ''])
				#ジャスティサー・トゥルーハート : [x]<b>雄叫び:</b>自分のヒーローパワーが強化版に代わる。
			elif ID == 'AT_133':
				cond1.append(['battlecry','', ''])
				#ガジェッツァンの槍試合選手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合__+1/+1を獲得する。
		elif 'BOT_' in ID:
			if ID == 'BOT_079':
				cond1.append(['battlecry','', ''])
				#忠実ロボ・ルミ : [x]<b>雄叫び:</b>味方のメカ1体に__+1/+1を付与する。
			elif ID == 'BOT_083':
				cond1.append(['battlecry','', ''])
				#毒物学者 : [x]<b>雄叫び:</b>自分の武器に___攻撃力+1を付与する。
			elif ID == 'BOT_243':
				cond1.append(['battlecry','', ''])
				#マイラ・ロットスプリング : [x]<b>雄叫び:</b><b>断末魔</b>を持つミニオンを1体<b>発見</b>する。さらにそのミニオンの__<b>断末魔</b>を獲得する。
			elif ID == 'BOT_270':
				cond1.append(['battlecry','', ''])
				#含み笑う発明家 : [x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。
			elif ID == 'BOT_283':
				cond1.append(['battlecry','', ''])
				#ホッピング・ホッパー : [x]<b>雄叫び:</b>この対戦で自分が手札から使用した他の「ホッピング・ホッパー」1体につき_+2/+2を獲得する。
			elif ID == 'BOT_288':
				cond1.append(['battlecry','', ''])
				#ラボの採用担当者 : [x]<b>雄叫び:</b>味方のミニオン1体のコピー3枚を____自分のデッキに混ぜる。
			elif ID == 'BOT_296':
				cond1.append(['battlecry','', ''])
				#オメガ・ディフェンダー : [x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_
			elif ID == 'BOT_308':
				cond1.append(['battlecry','', ''])
				#スプリング・ロケット : <b>雄叫び:</b>2ダメージを与える。
			elif ID == 'BOT_413':
				cond1.append(['battlecry','', ''])
				#ブレインストーマー : [x]<b>雄叫び:</b>自分の手札の呪文1枚につき_____体力+1を獲得する。
			elif ID == 'BOT_431':
				cond1.append(['battlecry','', ''])
				#グルグルグライダー : [x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を1体召喚する。
			elif ID == 'BOT_447':
				cond1.append(['battlecry','', ''])
				#結晶術師 : [x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_
			elif ID == 'BOT_448':
				cond1.append(['battlecry','', ''])
				#損傷したステゴトロン : <b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。
			elif ID == 'BOT_511':
				cond1.append(['battlecry','', ''])
				#シーフォーリウム・ボンバー : [x]<b>雄叫び:</b>相手のデッキに「爆弾」1枚を混ぜる。「爆弾」は引かれた際に爆発し__5ダメージを与える。
			elif ID == 'BOT_532':
				cond1.append(['battlecry','', ''])
				#エクスプローディネーター : [x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を___2体召喚する。
			elif ID == 'BOT_535':
				cond1.append(['battlecry','', ''])
				#マイクロロボ操縦者 : [x]<b>雄叫び:</b>1/1の「マイクロロボ」を___2体召喚する。
			elif ID == 'BOT_538':
				cond1.append(['battlecry','', ''])
				#スパーク・エンジン : [x]<b>雄叫び:</b><b>急襲</b>を持つ1/1の「スパーク」1体を____自分の手札に追加する。
			elif ID == 'BOT_539':
				cond1.append(['battlecry','', ''])
				#魔力ダイナモ : [x]<b>雄叫び:</b>コスト（5）以上の呪文を1枚<b>発見</b>する。
			elif ID == 'BOT_540':
				cond1.append(['battlecry','', ''])
				#電磁パルス工作員 : [x]<b>雄叫び:</b>__メカ1体を破壊する。
			elif ID == 'BOT_544':
				cond1.append(['battlecry','', ''])
				#逃走する試験体 : [x]<b>雄叫び:</b>合計6ダメージを自身を除く味方のミニオンにランダムに振り分ける。
			elif ID == 'BOT_550':
				cond1.append(['battlecry','', ''])
				#電気職工 : [x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__+1/+1を獲得する。
			elif ID == 'BOT_552':
				cond1.append(['battlecry','', ''])
				#天体配列者 : [x]<b>雄叫び:</b>味方に体力7のミニオンが3体以上いる場合全ての敵に_7ダメージを与える。
			elif ID == 'BOT_562':
				cond1.append(['battlecry','', ''])
				#カッパーテイルモドキ : [x]<b>雄叫び:</b>次の自分のターンまで__<b>隠れ身</b>を獲得する。
			elif ID == 'BOT_573':
				cond1.append(['battlecry','', ''])
				#実験台9号 : <b>雄叫び:</b>自分のデッキから異なる<b>秘策</b>を5枚引く。
			elif ID == 'BOT_907':
				cond1.append(['battlecry','', ''])
				#電設ロボ : <b>雄叫び:</b>自分の手札のメカ全てのコストを（1）減らす。
		elif 'BRM_' in ID:
			if ID == 'BRM_008':
				cond1.append(['battlecry','', ''])
				#ダークアイアン・スカルカー : [x]<b>雄叫び:</b>ダメージを受けていない敵のミニオン全てに____2ダメージを与える。
			elif ID == 'BRM_024':
				cond1.append(['battlecry','', ''])
				#ドラコニッド・クラッシャー : [x]<b>雄叫び:</b> 相手の体力が15以下の場合____+3/+3を獲得する。
			elif ID == 'BRM_026':
				cond1.append(['battlecry','', ''])
				#腹ペコのドラゴン : <b>雄叫び:</b> ランダムなコスト1のミニオン1体を相手の陣地に召喚する。
			elif ID == 'BRM_029':
				cond1.append(['battlecry','', ''])
				#レンド・ブラックハンド : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合<b>レジェンド</b>ミニオン1体を破壊する。
			elif ID == 'BRM_030':
				cond1.append(['battlecry','', ''])
				#ネファリアン : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムな呪文2枚を____自分の手札に追加する。
			elif ID == 'BRM_033':
				cond1.append(['battlecry','', ''])
				#ブラックウィングの技術者 : [x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合____+1/+1を獲得する。
			elif ID == 'BRM_034':
				cond1.append(['battlecry','', ''])
				#ブラックウィングの変性者 : [x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合_____3ダメージを与える。
		elif 'BT_' in ID:
			if ID == 'BT_010':
				cond1.append(['battlecry','', ''])
				#フェルフィンのナビ : <b>雄叫び:</b>自身を除く味方のマーロックに___+1/+1を付与する。
			elif ID == 'BT_126':
				cond1.append(['battlecry','', ''])
				#テロン・ゴアフィーンド : [x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。
			elif ID == 'BT_159':
				cond1.append(['battlecry','', ''])
				#テラーガードの逃亡者 : <b>雄叫び:</b>相手の陣地に1/1の「追手」を___3体召喚する。
			elif ID == 'BT_160':
				cond1.append(['battlecry','', ''])
				#錆鉄の狂信者 : [x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。
			elif ID == 'BT_702':
				cond1.append(['battlecry','', ''])
				#アッシュタン・スレイヤー : [x]<b>雄叫び:</b><b>隠れ身</b>状態のミニオン1体にこのターンの間、攻撃力+3と<b>無敵</b>を付与する。
			elif ID == 'BT_710':
				cond1.append(['battlecry','', ''])
				#グレイハート族の賢者 : [x]<b>雄叫び:</b>味方に<b>隠れ身</b>状態のミニオンがいる場合______カードを2枚引く。__
			elif ID == 'BT_711':
				cond1.append(['battlecry','', ''])
				#脳天直撃ガール : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合ミニオン1体を所有者の手札に戻す。そのコストは（1）増える。
			elif ID == 'BT_714':
				cond1.append(['battlecry','', ''])
				#冷たき影の紡ぎ手 : <b>雄叫び:</b>敵1体を<b>凍結</b>させる。
			elif ID == 'BT_717':
				cond1.append(['battlecry','', ''])
				#穴掘りスコーピッド : [x]<b>雄叫び:</b>2ダメージを与える。これにより対象が死んだ場合<b>隠れ身</b>を獲得する。
			elif ID == 'BT_720':
				cond1.append(['battlecry','', ''])
				#錆鉄騎の略奪者 : <b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。
			elif ID == 'BT_722':
				cond1.append(['battlecry','', ''])
				#ガーディアン改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>聖なる盾</b>を付与する。_
			elif ID == 'BT_723':
				cond1.append(['battlecry','', ''])
				#ロケット改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>急襲</b>を付与する。_
			elif ID == 'BT_724':
				cond1.append(['battlecry','', ''])
				#イセリアル改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。
			elif ID == 'BT_729':
				cond1.append(['battlecry','', ''])
				#荒野の看守 : [x]<b>雄叫び:</b>ミニオン1体と、同種族の他のミニオン全てに__3ダメージを与える。
			elif ID == 'BT_732':
				cond1.append(['battlecry','', ''])
				#鋼拾いのシヴァーラ : [x]<b>雄叫び:</b>合計6ダメージを自身を除くミニオンに____ランダムに振り分ける。_
			elif ID == 'BT_737':
				cond1.append(['battlecry','', ''])
				#マイエヴ・シャドウソング : [x]<b>雄叫び:</b>ミニオン1体を選択する。そのミニオンは2ターンの間<b>休眠状態</b>になる。
			elif ID == 'BT_850':
				cond1.append(['battlecry','', ''])
				#マグゼリドン : [x]<b>休眠状態</b>。<b>雄叫び:</b>敵の陣地に1/3の結界師を3体召喚する。それらが死んだ時全てのミニオンを破壊して目覚める。
		elif 'CFM_' in ID:
			if ID == 'CFM_063':
				cond1.append(['battlecry','', ''])
				#妙ちくりんな薬剤師 : [x]<b>雄叫び:</b> ミニオン1体の攻撃力と体力を入れ替える。
			elif ID == 'CFM_067':
				cond1.append(['battlecry','', ''])
				#ホーゼンの治療師 : [x]<b>雄叫び:</b> ミニオン1体の体力を____上限まで回復する。
			elif ID == 'CFM_321':
				cond1.append(['battlecry','', ''])
				#グライムストリートの情報屋 : [x]<b>雄叫び:</b>ハンター、パラディンまたはウォリアーの　カードを1枚<b>発見</b>する。
			elif ID == 'CFM_328':
				cond1.append(['battlecry','', ''])
				#闘技プロモーター : <b>雄叫び:</b> 味方に体力6以上のミニオンがいる場合カードを2枚引く。
			elif ID == 'CFM_342':
				cond1.append(['battlecry','', ''])
				#幸運のお守りのバッカニーア : [x]<b>雄叫び:</b>自分の武器の攻撃力が3以上ある場合____+4/+4を獲得する。
			elif ID == 'CFM_619':
				cond1.append(['battlecry','', ''])
				#カバールの薬剤師 : [x]<b>雄叫び:</b>ランダムなポーション1枚を自分の手札に追加する。
			elif ID == 'CFM_621':
				cond1.append(['battlecry','', ''])
				#カザカス : [x]<b>雄叫び:</b>自分のデッキに重複するカードがない場合_____即興呪文を1つ作成する。
			elif ID == 'CFM_647':
				cond1.append(['battlecry','', ''])
				#ブロウギル・スナイパー : [x]<b>雄叫び:</b> 1ダメージを与える。
			elif ID == 'CFM_648':
				cond1.append(['battlecry','', ''])
				#暗黒街の大物 : <b>雄叫び:</b>6/6のオーガを1体召喚する。
			elif ID == 'CFM_649':
				cond1.append(['battlecry','', ''])
				#カバールの飛脚 : [x]<b>雄叫び:</b>メイジ、プリーストまたはウォーロックの　カードを1枚<b>発見</b>する。
			elif ID == 'CFM_651':
				cond1.append(['battlecry','', ''])
				#ナーガの海賊 : [x]<b>雄叫び:</b>自分の武器に___攻撃力+1を付与する。
			elif ID == 'CFM_655':
				cond1.append(['battlecry','', ''])
				#有毒下水ウーズ : [x]<b>雄叫び:</b>敵の武器の耐久度を1減らす。
			elif ID == 'CFM_656':
				cond1.append(['battlecry','', ''])
				#裏街の探偵 : <b>雄叫び:</b> 敵のミニオンは<b>隠れ身</b>を失う。
			elif ID == 'CFM_659':
				cond1.append(['battlecry','', ''])
				#ガジェッツァンのセレブ : <b>雄叫び:</b>体力を#2回復する。
			elif ID == 'CFM_667':
				cond1.append(['battlecry','', ''])
				#爆弾部隊 : [x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。
			elif ID == 'CFM_668':
				cond1.append(['battlecry','', ''])
				#ドッペルギャングスター : [x]<b>雄叫び:</b>このミニオンのコピーを2体召喚する。
			elif ID == 'CFM_672':
				cond1.append(['battlecry','', ''])
				#マダム・ゴヤ : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンを自分のデッキのミニオン1体と入れ替える。
			elif ID == 'CFM_685':
				cond1.append(['battlecry','', ''])
				#ドン・ハン＝チョー : <b>雄叫び:</b>自分の手札のランダムなミニオン1体に+5/+5を付与する。
			elif ID == 'CFM_688':
				cond1.append(['battlecry','', ''])
				#トゲ付きのホグライダー : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。
			elif ID == 'CFM_694':
				cond1.append(['battlecry','', ''])
				#影の師匠 : [x]<b>雄叫び:</b><b>隠れ身</b>を持つミニオン1体に　+2/+2を付与する。
			elif ID == 'CFM_715':
				cond1.append(['battlecry','', ''])
				#翡翠の精霊 : [x]<b>雄叫び:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び:</b><b>翡翠のゴーレム</b>を1体召喚する。
			elif ID == 'CFM_790':
				cond1.append(['battlecry','', ''])
				#ドブネズミ : [x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。
			elif ID == 'CFM_806':
				cond1.append(['battlecry','', ''])
				#ラシオン : [x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。
			elif ID == 'CFM_809':
				cond1.append(['battlecry','', ''])
				#タナリスのホグチョッパー : [x]<b>雄叫び:</b>相手が手札を1枚も持っていない場合<b>突撃</b>を獲得する。
			elif ID == 'CFM_810':
				cond1.append(['battlecry','', ''])
				#ピチピチレザーのホグリーダー : [x]<b>雄叫び:</b>相手の手札が6枚以上ある場合_____<b>突撃</b>を獲得する。
			elif ID == 'CFM_852':
				cond1.append(['battlecry','', ''])
				#蓮華密使 : [x]<b>雄叫び:</b>ドルイド、ローグまたはシャーマンの_____カードを1枚<b>発見</b>する。
			elif ID == 'CFM_853':
				cond1.append(['battlecry','', ''])
				#グライムストリートの運び屋 : <b>雄叫び:</b>自分の手札のランダムなミニオン1体に+1/+1を付与する。
			elif ID == 'CFM_855':
				cond1.append(['battlecry','HeHasDeathrattle(game)', 'silence'])
				#デファイアスの掃除屋 : [x]<b>雄叫び:</b><b>断末魔</b>を持つミニオン1体を<b>沈黙</b>させる。
		elif 'CS2_' in ID:
			if ID == 'CS2_117':
				cond1.append(['battlecry','', ''])
				#大地の円環の遠見師 : <b>雄叫び:</b>体力を#3回復する。
			elif ID == 'CS2_141':
				cond1.append(['battlecry','', ''])
				#アイアンフォージのライフル兵 : <b>雄叫び:</b> 1ダメージを与える。
			elif ID == 'CS2_147':
				cond1.append(['battlecry','', ''])
				#ノームの発明家 : <b>雄叫び:</b> カードを1枚引く。
			elif ID == 'CS2_150':
				cond1.append(['battlecry','', ''])
				#ストームパイクのコマンドー : <b>雄叫び:</b> 2ダメージを与える。
			elif ID == 'CS2_151':
				cond1.append(['battlecry','', ''])
				#シルバーハンド騎士 : [x]<b>雄叫び:</b>2/2の従騎士を1体召喚する。
			elif ID == 'CS2_181':
				cond1.append(['battlecry','', ''])
				#傷を負った剣匠 : <b>雄叫び:</b> 自身に4ダメージを与える。
			elif ID == 'CS2_188':
				cond1.append(['battlecry','', ''])
				#鬼軍曹 : [x]<b>雄叫び:</b>このターンの間ミニオン1体に______攻撃力+2を付与する。_
			elif ID == 'CS2_189':
				cond1.append(['battlecry','', ''])
				#エルフの射手 : <b>雄叫び:</b> 1ダメージを与える。
			elif ID == 'CS2_196':
				cond1.append(['battlecry','', ''])
				#レイザーフェン・ハンター : [x]<b>雄叫び:</b> 1/1のイノシシを1体召喚する。
			elif ID == 'CS2_203':
				cond1.append(['battlecry','heHasMinion(game)', 'silence'])
				#鉄嘴のフクロウ : [x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。
			elif ID == 'CS2_226':
				cond1.append(['battlecry','', ''])
				#フロストウルフの将軍 : [x]<b>雄叫び:</b> 戦場にいる味方のミニオン1体につき____+1/+1を獲得する。
		elif 'DAL_' in ID:
			if ID == 'DAL_058':
				cond1.append(['battlecry','', ''])
				#ヤジロボ : <b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。
			elif ID == 'DAL_077':
				cond1.append(['battlecry','', ''])
				#毒々フィン : [x]<b>雄叫び:</b>味方のマーロック1体に<b>猛毒</b>を付与する。
			elif ID == 'DAL_078':
				cond1.append(['battlecry','', ''])
				#旅の治療師 : <b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。
			elif ID == 'DAL_081':
				cond1.append(['battlecry','', ''])
				#魔除けの宝石職人 : [x]<b>雄叫び:</b>次の自分のターンまで自分のヒーローは呪文とヒーローパワーの標的にならない。
			elif ID == 'DAL_086':
				cond1.append(['battlecry','', ''])
				#サンリーヴァーのスパイ : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合____+1/+1を獲得する。
			elif ID == 'DAL_087':
				cond1.append(['battlecry','', ''])
				#ヘンチ・クランの妖婆 : [x]<b>雄叫び:</b>種族が「全て」である1/1の「融合体」を2体召喚する。
			elif ID == 'DAL_089':
				cond1.append(['battlecry','', ''])
				#呪文書綴じ師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。
			elif ID == 'DAL_095':
				cond1.append(['battlecry','', ''])
				#ヴァイオレット監獄の魔剣士 : [x]<b>雄叫び:</b>自分の手札の呪文1枚につき____攻撃力+1を獲得する。
			elif ID == 'DAL_400':
				cond1.append(['battlecry','', ''])
				#悪党同盟の電線ネズミ : [x]<b>雄叫び:</b><b>悪の手先</b>1体を自分の手札に追加する。
			elif ID == 'DAL_416':
				cond1.append(['battlecry','', ''])
				#ヘンチ・クランの強盗 : [x]<b>雄叫び:</b>他のクラスの呪文を1つ<b>発見</b>する。
			elif ID == 'DAL_417':
				cond1.append(['battlecry','', ''])
				#強盗王トグワグル : [x]<b>雄叫び:</b>味方に<b>悪の手先</b>がいる場合、素敵な_____宝物を1つ選択する。
			elif ID == 'DAL_538':
				cond1.append(['battlecry','', ''])
				#こっそり妨害工作員 : [x]<b>雄叫び:</b>相手は手札のランダムな呪文を1つ使用する。__<i>（対象はランダムに選択）</i>
			elif ID == 'DAL_539':
				cond1.append(['battlecry','', ''])
				#サンリーヴァーの戦魔術師 : [x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__4ダメージを与える。
			elif ID == 'DAL_544':
				cond1.append(['battlecry','', ''])
				#ポーション売り : [x]<b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
			elif ID == 'DAL_546':
				cond1.append(['battlecry','', ''])
				#バリスタのリンチェン : [x]<b>雄叫び:</b>自身を除く味方の<b>雄叫び</b>を持つミニオン全てのコピーを1枚ずつ______自分の手札に追加する。_
			elif ID == 'DAL_554':
				cond1.append(['battlecry','', ''])
				#シェフ・ノミ : [x]<b>雄叫び:</b>自分のデッキが空の場合6/6の「油火災のエレメンタル」を6体召喚する。
			elif ID == 'DAL_560':
				cond1.append(['battlecry','', ''])
				#酒場のヒロイック女将 : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_
			elif ID == 'DAL_565':
				cond1.append(['battlecry','', ''])
				#ポータル・オーバーフィーンド : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
			elif ID == 'DAL_582':
				cond1.append(['battlecry','', ''])
				#ポータルの番人 : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
			elif ID == 'DAL_714':
				cond1.append(['battlecry','', ''])
				#最下層の故買屋 : [x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合+1/+1と<b>急襲</b>を獲得する。
			elif ID == 'DAL_735':
				cond1.append(['battlecry','HasNeedSilenceMinion', 'silence'])
				#ダラランの司書 : <b>雄叫び:</b>隣接するミニオンを<b>沈黙</b>させる。
			elif ID == 'DAL_736':
				cond1.append(['battlecry','', ''])
				#文書管理官エリシアーナ : [x]<b>雄叫び:</b>カードを5枚<b>発見</b>する。そのコピー2枚ずつを自分のデッキと置き換える。
			elif ID == 'DAL_744':
				cond1.append(['battlecry','', ''])
				#無貌レイジャー : [x]<b>雄叫び:</b>味方のミニオン1体の___体力をコピーする。
			elif ID == 'DAL_747':
				cond1.append(['battlecry','', ''])
				#フライトマスター : [x]<b>雄叫び:</b>各プレイヤーの陣地に2/2の「グリフォン」を1体ずつ召喚する。
			elif ID == 'DAL_751':
				cond1.append(['battlecry','', ''])
				#狂気の召喚師 : [x]<b>雄叫び:</b>各プレイヤーの陣地に1/1の「インプ」を____可能な限り召喚する。
			elif ID == 'DAL_752':
				cond1.append(['battlecry','', ''])
				#ジェペット・ジョイバズ : [x]<b>雄叫び:</b>自分のデッキからミニオンを2体引く。それらの攻撃力、体力、コストを1に変える。
		elif 'DRG_' in ID:
			if ID == 'DRG_027':
				cond1.append(['battlecry','', ''])
				#陰の殺し屋 : [x]<b>雄叫び:</b>既に2回<b>祈願</b>していた場合「コイン」3枚を____自分の手札に追加する。
			elif ID == 'DRG_034':
				cond1.append(['battlecry','', ''])
				#密航者 : [x]<b>雄叫び:</b>自分のデッキに対戦開始時になかったカードがある場合、それらを2枚まで引く。
			elif ID == 'DRG_035':
				cond1.append(['battlecry','', ''])
				#ブラッドセイルのスカイ賊 : [x]<b>雄叫び:</b>1/1の海賊2体を__自分の手札に追加する。
			elif ID == 'DRG_037':
				cond1.append(['battlecry','', ''])
				#フリック・スカイシヴ : [x]<b>雄叫び:</b>ミニオン1体と同名のミニオン全てを破壊する<i>（居場所は問わない）</i>。
			elif ID == 'DRG_050':
				cond1.append(['battlecry','', ''])
				#心血注ぐ献身者 : <b>急襲</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
			elif ID == 'DRG_054':
				cond1.append(['battlecry','', ''])
				#ぽっちゃりチビドラゴン : <b>雄叫び:</b>カードを1枚引く。
			elif ID == 'DRG_055':
				cond1.append(['battlecry','', ''])
				#財宝荒らし : [x]<b>雄叫び:</b>自分の破壊された___武器1つを装備する。
			elif ID == 'DRG_059':
				cond1.append(['battlecry','', ''])
				#ゴボグライダー技士 : [x]<b>雄叫び:</b>自分の陣地にメカがいる場合+1/+1と<b>急襲</b>を獲得する。
			elif ID == 'DRG_060':
				cond1.append(['battlecry','', ''])
				#ファイアーホーク : [x]<b>雄叫び:</b>相手の手札1枚につき__攻撃力+1を獲得する。
			elif ID == 'DRG_062':
				cond1.append(['battlecry','', ''])
				#ワームレストの浄術師 : [x]<b>雄叫び:</b>自分のデッキの中立カード全てをランダムな自分のクラスのカードに変身させる。
			elif ID == 'DRG_063':
				cond1.append(['battlecry','', ''])
				#ドラゴンモーの密猟者 : <b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。
			elif ID == 'DRG_064':
				cond1.append(['battlecry','', ''])
				#ズルドラクの儀式官 : [x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__
			elif ID == 'DRG_067':
				cond1.append(['battlecry','', ''])
				#トロルのコウモリ騎兵 : <b>雄叫び:</b>ランダムな敵のミニオン1体に__3ダメージを与える。
			elif ID == 'DRG_069':
				cond1.append(['battlecry','', ''])
				#プレートブレイカー : [x]<b>雄叫び:</b>相手の装甲を破壊する。
			elif ID == 'DRG_070':
				cond1.append(['battlecry','', ''])
				#ドラゴンブリーダー : <b>雄叫び:</b>味方のドラゴン1体を選択する。そのコピー1体を自分の手札に追加する。
			elif ID == 'DRG_072':
				cond1.append(['battlecry','', ''])
				#スカイフィン : <b>雄叫び:</b>自分の手札にドラゴンがいる場合ランダムなマーロックを2体召喚する。
			elif ID == 'DRG_074':
				cond1.append(['battlecry','', ''])
				#擬装した飛行船 : [x]<b>雄叫び:</b>次の自分のターンまで自身を除く味方のメカに<b>隠れ身</b>を付与する。
			elif ID == 'DRG_075':
				cond1.append(['battlecry','', ''])
				#コバルト・スペルキン : [x]<b>雄叫び:</b>自分のクラスのコスト1の呪文2枚を自分の手札に追加する。
			elif ID == 'DRG_076':
				cond1.append(['battlecry','', ''])
				#無貌の変性者 : <b>急襲</b>、<b>雄叫び:</b>味方のミニオン1体をこのミニオンのコピーに変身させる。
			elif ID == 'DRG_077':
				cond1.append(['battlecry','', ''])
				#ウトガルドのグラップル狙撃手 : [x]<b>雄叫び:</b>両プレイヤーはカードを1枚引く。それがドラゴンだった場合召喚する。
			elif ID == 'DRG_081':
				cond1.append(['battlecry','', ''])
				#スケイルライダー : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____2ダメージを与える。
			elif ID == 'DRG_082':
				cond1.append(['battlecry','', ''])
				#コボルトの棒ドロ : <b>雄叫び:</b>相手の武器を奪う。
			elif ID == 'DRG_084':
				cond1.append(['battlecry','', ''])
				#触手の脅異 : [x]<b>雄叫び:</b>各プレイヤーはカードを1枚ずつ引く。それらの____コストを入れ替える。__
			elif ID == 'DRG_086':
				cond1.append(['battlecry','', ''])
				#クロマティックの卵 : [x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！
			elif ID == 'DRG_089':
				cond1.append(['battlecry','', ''])
				#竜の女王アレクストラーザ : [x]<b>雄叫び:</b>_自分のデッキに重複するカードがない場合自身を除くランダムなドラゴン2体を自分の手札に追加する。____それらのコストは（1）になる。
			elif ID == 'DRG_099':
				cond1.append(['battlecry','', ''])
				#クロンクス・ドラゴンフーフ : [x]<b>雄叫び:</b>ガラクロンドを引く。自分が既にガラクロンドの場合ガラクロンドの大禍を引き起こす。
			elif ID == 'DRG_213':
				cond1.append(['battlecry','', ''])
				#双暴帝 : [x]<b>雄叫び:</b>ランダムな敵のミニオン2体に_____4ダメージずつ与える。
			elif ID == 'DRG_242':
				cond1.append(['battlecry','', ''])
				#ガラクロンドの盾 : <b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
			elif ID == 'DRG_257':
				cond1.append(['battlecry','', ''])
				#フリズ・キンドルルースト : <b>雄叫び:</b>自分のデッキのドラゴン全てのコストを（2）減らす。
			elif ID == 'DRG_401':
				cond1.append(['battlecry','', ''])
				#灰色の魔法使い : [x]<b>雄叫び:</b>次の自分のターンまで相手とヒーロー______パワーを交換する。_
			elif ID == 'DRG_402':
				cond1.append(['battlecry','', ''])
				#サスロヴァール : [x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのコピーを自分の手札、デッキ、陣地に_____それぞれ1体ずつ追加する。
			elif ID == 'DRG_403':
				cond1.append(['battlecry','', ''])
				#ブロートーチ妨害工作員 : <b>雄叫び:</b>相手が次に使うヒーローパワーのコストは（3）。
		elif ID == 'DS1_055':
				cond1.append(['battlecry','', ''])
				#ダークスケイルの治療師 : <b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
		elif 'EX1_' in ID:
			if ID == 'EX1_002':
				cond1.append(['battlecry','', ''])
				#黒騎士 : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。
			elif ID == 'EX1_005':
				cond1.append(['battlecry','', ''])
				#大物ハンター : [x]<b>雄叫び:</b>攻撃力7以上のミニオン1体を破壊する。
			elif ID == 'EX1_011':
				cond1.append(['battlecry','', ''])
				#ヴードゥーの呪術医 : <b>雄叫び:</b>体力を#2回復する。
			elif ID == 'EX1_014':
				cond1.append(['battlecry','', ''])
				#キング・ムクラ : <b>雄叫び:</b> 敵の手札に「バナナ」2枚を追加する。
			elif ID == 'EX1_015':
				cond1.append(['battlecry','', ''])
				#初級エンジニア : <b>雄叫び:</b> カードを1枚引く。
			elif ID == 'EX1_019':
				cond1.append(['battlecry','', ''])
				#シャタード・サンの聖職者 : [x]<b>雄叫び:</b>味方のミニオン1体に +1/+1を 付与する。
			elif ID == 'EX1_025':
				cond1.append(['battlecry','', ''])
				#ミニドラゴン・メカニック : [x]<b>雄叫び:</b> 2/1のメカ・ミニドラゴンを[b]1体召喚する。
			elif ID == 'EX1_043':
				cond1.append(['battlecry','', ''])
				#トワイライト・ドレイク : <b>雄叫び:</b> 自分の手札1枚につき体力+1を獲得する。
			elif ID == 'EX1_046':
				cond1.append(['battlecry','', ''])
				#ダークアイアンのドワーフ : [x]<b>雄叫び:</b> このターンの間ミニオン1体に　攻撃力+2を付与する。
			elif ID == 'EX1_048':
				cond1.append(['battlecry','heHasNonVanilla(game)', 'silence'])
				#スペルブレイカー : [x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。
			elif ID == 'EX1_049':
				cond1.append(['battlecry','', ''])
				#若き酒造大師 : <b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。
			elif ID == 'EX1_050':
				cond1.append(['battlecry','', ''])
				#コールドライトの託宣師 : [x]<b>雄叫び:</b> 各プレイヤーはカードを2枚ずつ引く。
			elif ID == 'EX1_057':
				cond1.append(['battlecry','', ''])
				#老練の酒造大師 : <b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。
			elif ID == 'EX1_058':
				cond1.append(['battlecry','', ''])
				#サンフューリーの護衛 : [x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。
			elif ID == 'EX1_059':
				cond1.append(['battlecry','', ''])
				#イカレた錬金術師 : [x]<b>雄叫び:</b> ミニオン1体の攻撃力と体力を入れ替える。
			elif ID == 'EX1_066':
				cond1.append(['battlecry','', ''])
				#酸性沼ウーズ : <b>雄叫び:</b> 敵の武器を破壊する。
			elif ID == 'EX1_082':
				cond1.append(['battlecry','', ''])
				#マッドボンバー : [x]<b>雄叫び:</b>合計3ダメージを自身を除くキャラクターに____ランダムに振り分ける。
			elif ID == 'EX1_083':
				cond1.append(['battlecry','', ''])
				#ティンクマスター・オーバースパーク : [x]<b>雄叫び:</b> 自身以外のランダムなミニオン1体を5/5のデビルサウルスか_____1/1のリスに変身させる。_
			elif ID == 'EX1_085':
				cond1.append(['battlecry','', ''])
				#精神支配技士 : [x]<b>雄叫び:</b> 戦場に敵のミニオンが4体以上いる場合ランダムな1体を自分の味方にする。
			elif ID == 'EX1_089':
				cond1.append(['battlecry','', ''])
				#魔力のゴーレム : [x]<b>雄叫び:</b>相手にマナクリスタルを1個付与する。
			elif ID == 'EX1_093':
				cond1.append(['battlecry','', ''])
				#アルガスの守護者 : <b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。
			elif ID == 'EX1_103':
				cond1.append(['battlecry','', ''])
				#コールドライトの予言者 : [x]<b>雄叫び:</b> 自身を除く味方のマーロックに_____体力+2を付与する。
			elif ID == 'EX1_112':
				cond1.append(['battlecry','', ''])
				#ゲルビン・メカトルク : <b>雄叫び:</b> すばらしい発明品を1体召喚する。
			elif ID == 'EX1_116':
				cond1.append(['battlecry','', ''])
				#リロイ・ジェンキンス : [x]<b>突撃</b>、<b>雄叫び:</b> 敵の陣地に1/1のチビドラゴンを2体召喚する。
			elif ID == 'EX1_133':
				cond1.append(['battlecry','', ''])
				#地獄送りの刃 : [x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。
			elif ID == 'EX1_186':
				cond1.append(['battlecry','', ''])
				#SI:7潜入工作員 : [x]<b>雄叫び:</b>ランダムな敵の___<b>秘策</b>1つを破壊する。
			elif ID == 'EX1_188':
				cond1.append(['battlecry','', ''])
				#荒野の口取り : [x]<b>雄叫び:</b>ランダムな獣を1体召喚する。
			elif ID == 'EX1_189':
				cond1.append(['battlecry','', ''])
				#ブライトウィング : <b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。
			elif ID == 'EX1_190':
				cond1.append(['battlecry','', ''])
				#大審問官ホワイトメイン : <b>雄叫び:</b>このターンに死亡した味方のミニオン全てを召喚する。
			elif ID == 'EX1_191':
				cond1.append(['battlecry','', ''])
				#病魔の運び手 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>猛毒</b>を付与する。
			elif ID == 'EX1_283':
				cond1.append(['battlecry','', ''])
				#フロスト・エレメンタル : [x]<b>雄叫び:</b> キャラクター1体を<b>凍結</b>させる。
			elif ID == 'EX1_284':
				cond1.append(['battlecry','', ''])
				#アジュア・ドレイク : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。
			elif ID == 'EX1_506':
				cond1.append(['battlecry','', ''])
				#マーロックのタイドハンター : [x]<b>雄叫び:</b> 1/1のマーロックの 偵察兵を1体召喚する。
			elif ID == 'EX1_558':
				cond1.append(['battlecry','', ''])
				#ハリソン・ジョーンズ : <b>雄叫び:</b> 敵の武器を破壊しその耐久度に等しい枚数のカードを引く。
			elif ID == 'EX1_561':
				cond1.append(['battlecry','', ''])
				#アレクストラーザ : [x]<b>雄叫び:</b>ヒーロー1人の残り__体力を15にする。
			elif ID == 'EX1_562':
				cond1.append(['battlecry','', ''])
				#オニクシア : [x]<b>雄叫び:</b>自分の陣地が満員になる数の1/1のチビドラゴンを召喚する。
			elif ID == 'EX1_564':
				cond1.append(['battlecry','', ''])
				#無貌の操り手 : <b>雄叫び:</b> ミニオン1体を選択しそのミニオンのコピーに変化する。
			elif ID == 'EX1_583':
				cond1.append(['battlecry','', ''])
				#エルーンのプリーステス : <b>雄叫び:</b>自分のヒーローの体力を#4回復する。
			elif ID == 'EX1_584':
				cond1.append(['battlecry','', ''])
				#老練のメイジ : [x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。
			elif ID == 'EX1_590':
				cond1.append(['battlecry','', ''])
				#ブラッドナイト : [x]<b>雄叫び:</b> 全てのミニオンは<b>聖なる盾</b>を失う。失われた聖なる盾1つにつき+3/+3を獲得する。
			elif ID == 'EX1_593':
				cond1.append(['battlecry','', ''])
				#ナイトブレード : [x]<b>雄叫び: </b>敵のヒーローに3ダメージを与える。
		elif 'FP1_' in ID:
			if ID == 'FP1_003':
				cond1.append(['battlecry','', ''])
				#反響ウーズ : <b>雄叫び:</b> このターンの終了時にこのミニオンと全く同じコピーを1体召喚する。
			elif ID == 'FP1_016':
				cond1.append(['battlecry','HasNeedSilenceMinion', 'silence'])
				#泣き叫ぶ魂 : [x]<b>雄叫び: </b>自身を除く味方のミニオンを_____<b>沈黙</b>させる。
			elif ID == 'FP1_030':
				cond1.append(['battlecry','', ''])
				#ロウゼブ : <b>雄叫び:</b> 次のターン敵の呪文のコストが（5）増える。
		elif 'GIL_' in ID:
			if ID == 'GIL_124':
				cond1.append(['battlecry','', ''])
				#苔むしたモノノケ : [x]<b>雄叫び:</b>自身を除く攻撃力2以下のミニオンを全て破壊する。
			elif ID == 'GIL_125':
				cond1.append(['battlecry','', ''])
				#いかれ帽子屋 : [x]<b>雄叫び:</b>自身を除くミニオンに帽子を3個ランダムに投げる。帽子はそれぞれ+1/+1を付与する。
			elif ID == 'GIL_198':
				cond1.append(['battlecry','', ''])
				#アザリナ・ソウルシーフ : [x]<b>雄叫び:</b>自分の手札全てを相手の手札全てのコピーに置き換える。
			elif ID == 'GIL_212':
				cond1.append(['battlecry','', ''])
				#鴉使い : [x]<b>雄叫び:</b>ランダムなコスト1のミニオン2体を自分の手札に追加する。
			elif ID == 'GIL_213':
				cond1.append(['battlecry','', ''])
				#毛むくじゃらのミスティック : [x]<b>雄叫び:</b>ランダムなコスト2の___ミニオン1体を各プレイヤーの手札に追加する。
			elif ID == 'GIL_526':
				cond1.append(['battlecry','', ''])
				#ワームガード : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。
			elif ID == 'GIL_561':
				cond1.append(['battlecry','', ''])
				#ブラックワルド・ピクシー : [x]<b>雄叫び:</b>自分のヒーローパワーを再度使用可能にする。
			elif ID == 'GIL_578':
				cond1.append(['battlecry','', ''])
				#アッシュモア伯爵夫人 : [x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。
			elif ID == 'GIL_581':
				cond1.append(['battlecry','', ''])
				#サンドバインダー : [x]<b>雄叫び:</b>自分のデッキからエレメンタル_を1体引く。
			elif ID == 'GIL_584':
				cond1.append(['battlecry','', ''])
				#ウィッチウッドの笛吹き : [x]<b>雄叫び:</b>自分のデッキから最もコストが低い____ミニオンを1体引く。
			elif ID == 'GIL_598':
				cond1.append(['battlecry','', ''])
				#テス・グレイメイン : [x]<b>雄叫び:</b>この対戦で自分が手札から使用した他のクラスのカード全てを再度使用する<i>（対象はランダムに選択される）</i>。
			elif ID == 'GIL_601':
				cond1.append(['battlecry','', ''])
				#スケイルワーム : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。
			elif ID == 'GIL_614':
				cond1.append(['battlecry','', ''])
				#ヴードゥー人形 : [x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。
			elif ID == 'GIL_622':
				cond1.append(['battlecry','', ''])
				#ライフドリンカー : [x]<b>雄叫び:</b>敵のヒーローに3ダメージを与える。自分のヒーローの体力を#3回復する。
			elif ID == 'GIL_623':
				cond1.append(['battlecry','', ''])
				#ウィッチウッドのグリズリー : [x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。
			elif ID == 'GIL_624':
				cond1.append(['battlecry','', ''])
				#ナイトプロウラー : [x]<b>雄叫び:</b>戦場に他のミニオンがいない場合、+3/+3を獲得する。
			elif ID == 'GIL_648':
				cond1.append(['battlecry','', ''])
				#ギルニーアスの警部 : <b>雄叫び:</b>敵の<b>秘策</b>全てを破壊する。
			elif ID == 'GIL_677':
				cond1.append(['battlecry','', ''])
				#貌を蒐めるもの : [x]<b>木霊</b>、<b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。
			elif ID == 'GIL_682':
				cond1.append(['battlecry','', ''])
				#マックハンター : [x]<b>急襲</b>、<b>雄叫び:</b>相手の陣地に2/1の「マックリング」_を2体召喚する。
			elif ID == 'GIL_683':
				cond1.append(['battlecry','', ''])
				#沼地のドレイク : [x]<b>雄叫び:</b>相手の陣地に<b>猛毒</b>を持つ2/1の「ドレイクスレイヤー」を1体召喚する。
			elif ID == 'GIL_815':
				cond1.append(['battlecry','', ''])
				#悪意の銀行家 : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのコピー1体を___自分のデッキに混ぜる。
			elif ID == 'GIL_827':
				cond1.append(['battlecry','', ''])
				#ブリンク・フォックス : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
		elif 'GVG_' in ID:
			if ID == 'GVG_023':
				cond1.append(['battlecry','', ''])
				#ゴブリン式全自動散髪機 : [x]<b>雄叫び:</b> 自分の武器に攻撃力+1を__付与する。
			elif ID == 'GVG_069':
				cond1.append(['battlecry','', ''])
				#骨董品のヒールロボ : <b>雄叫び:</b>自分のヒーローの体力を#8回復する。
			elif ID == 'GVG_074':
				cond1.append(['battlecry','', ''])
				#ケザンのミスティック : <b>雄叫び:</b> 敵のランダムな<b>秘策</b>1つを自分のものにする。
			elif ID == 'GVG_090':
				cond1.append(['battlecry','', ''])
				#マッダーボンバー : [x]<b>雄叫び:</b>合計6ダメージを自身を除くキャラクターに____ランダムに振り分ける。
			elif ID == 'GVG_092':
				cond1.append(['battlecry','', ''])
				#ノームの実験者 : [x]<b>雄叫び:</b> カードを1枚引く。そのカードがミニオンだった場合、そのカードを________ニワトリに変身させる。__
			elif ID == 'GVG_097':
				cond1.append(['battlecry','', ''])
				#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
			elif ID == 'GVG_099':
				cond1.append(['battlecry','', ''])
				#ボム・ロバー : <b>雄叫び:</b> ランダムな敵のミニオン1体に4ダメージを与える。
			elif ID == 'GVG_102':
				cond1.append(['battlecry','', ''])
				#ティンカータウンの技術者 : <b>雄叫び:</b> 味方にメカがいる場合+1/+1を獲得しさらに自分の手札に<b>スペアパーツ</b>1枚を追加する。
			elif ID == 'GVG_107':
				cond1.append(['battlecry','', ''])
				#エンハンス・オ・メカーノ : <b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>
			elif ID == 'GVG_108':
				cond1.append(['battlecry','', ''])
				#リコンボビュレイター : [x]<b>雄叫び:</b> 味方のミニオン1体を、ランダムな同コストのミニオンに変身させる。
			elif ID == 'GVG_110':
				cond1.append(['battlecry','', ''])
				#ドクター・ブーム : <b>雄叫び:</b> 1/1のブームロボを2体召喚する。<i>警告: ロボは爆発する場合がある。</i>
			elif ID == 'GVG_119':
				cond1.append(['battlecry','', ''])
				#ブリングトロン3000 : <b>雄叫び:</b> 各プレイヤーはランダムな武器を装備する。
			elif ID == 'GVG_120':
				cond1.append(['battlecry','', ''])
				#ヒーメット・ネッシングウェアリー : <b>雄叫び:</b> 獣1体を破壊する。
		elif 'ICC_' in ID:
			if ID == 'ICC_018':
				cond1.append(['battlecry','', ''])
				#ぶんどり幽霊船員 : [x]<b>雄叫び:</b>自分の武器の値に等しい攻撃力と　体力を獲得する。
			elif ID == 'ICC_025':
				cond1.append(['battlecry','', ''])
				#ガラガラガイコツ : [x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。
			elif ID == 'ICC_026':
				cond1.append(['battlecry','', ''])
				#非情の死霊術師 : [x]<b>雄叫び:</b>1/1のスケルトンを2体召喚する。
			elif ID == 'ICC_028':
				cond1.append(['battlecry','', ''])
				#サンボーン・ヴァルキル : [x]<b>雄叫び:</b>隣接するミニオンに　体力+2を付与する。
			elif ID == 'ICC_092':
				cond1.append(['battlecry','', ''])
				#アケラスの古残兵 : <b>雄叫び:</b>味方のミニオン1体に攻撃力+1を付与する。
			elif ID == 'ICC_093':
				cond1.append(['battlecry','', ''])
				#タスカーの漁師 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。
			elif ID == 'ICC_094':
				cond1.append(['battlecry','', ''])
				#フォールン・サンの聖職者 : [x]<b>雄叫び:</b>味方のミニオン1体に　+1/+1を付与する。
			elif ID == 'ICC_096':
				cond1.append(['battlecry','', ''])
				#タタラボッチ : <b>雄叫び:</b>自分の手札の武器を全て破棄しそれらの攻撃力と耐久度を獲得する。
			elif ID == 'ICC_098':
				cond1.append(['battlecry','', ''])
				#墓に潜むもの : [x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。
			elif ID == 'ICC_257':
				cond1.append(['battlecry','', ''])
				#死体蘇生者 : [x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。
			elif ID == 'ICC_466':
				cond1.append(['battlecry','', ''])
				#サロナイト鉱山の奴隷 : [x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。
			elif ID == 'ICC_467':
				cond1.append(['battlecry','', ''])
				#ネルビアンの説凶師 : [x]<b>雄叫び:</b>味方のミニオン1体にこのターンの間<b>無敵</b>を付与する。
			elif ID == 'ICC_701':
				cond1.append(['battlecry','', ''])
				#待ち伏せのガイスト : <b>雄叫び:</b>両プレイヤーの手札とデッキのコスト1の呪文を全て破壊する。
			elif ID == 'ICC_705':
				cond1.append(['battlecry','', ''])
				#ボーンメア : [x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。
			elif ID == 'ICC_810':
				cond1.append(['battlecry','', ''])
				#斧死なる断罪者 : [x]<b>雄叫び:</b>自分の手札の<b>生命奪取</b>を持つランダムなミニオン1体に+2/+2を付与する。
			elif ID == 'ICC_811':
				cond1.append(['battlecry','', ''])
				#リリアン・ヴォス : [x]<b>雄叫び:</b>自分の手札の呪文全てを<i>相手のクラスの</i>ランダムな呪文と置き換える。
			elif ID == 'ICC_850':
				cond1.append(['battlecry','', ''])
				#シャドウブレード : [x]<b>雄叫び:</b>自分のヒーローはこのターンの間<b>無敵</b>。
			elif ID == 'ICC_851':
				cond1.append(['battlecry','', ''])
				#ケレセス公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト2のカードがない場合、自分のデッキのミニオン全てに+1/+1を付与する。
			elif ID == 'ICC_852':
				cond1.append(['battlecry','', ''])
				#タルダラム公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト3のカードがない場合選択したミニオンの3/3のコピーに変身する。
			elif ID == 'ICC_853':
				cond1.append(['battlecry','', ''])
				#ヴァラナール公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。
			elif ID == 'ICC_855':
				cond1.append(['battlecry','', ''])
				#ヒルドニル・フロストライダール : <b>雄叫び:</b>自身を除く味方のミニオンを<b>凍結</b>させる。
			elif ID == 'ICC_904':
				cond1.append(['battlecry','', ''])
				#骸骨の魔女 : [x]<b>雄叫び:</b>このターンに死亡したミニオン1体につき　+1/+1を獲得する。
			elif ID == 'ICC_912':
				cond1.append(['battlecry','', ''])
				#躯の駆り手 : [x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。
		elif 'KAR_' in ID:
			if ID == 'KAR_030a':
				cond1.append(['battlecry','', ''])
				#食糧庫蜘蛛 : <b>雄叫び:</b>1/3の蜘蛛を1体召喚する。
			elif ID == 'KAR_033':
				cond1.append(['battlecry','', ''])
				#ブック・ワーム : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力3以下の敵の______ミニオン1体を破壊する。_
			elif ID == 'KAR_037':
				cond1.append(['battlecry','', ''])
				#番鳥 : <b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。
			elif ID == 'KAR_041':
				cond1.append(['battlecry','', ''])
				#堀に潜むもの : <b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。
			elif ID == 'KAR_061':
				cond1.append(['battlecry','', ''])
				#キュレーター : [x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。
			elif ID == 'KAR_062':
				cond1.append(['battlecry','', ''])
				#ネザースパイトの歴史家 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合____ドラゴン1体を<b>発見</b>する。
			elif ID == 'KAR_069':
				cond1.append(['battlecry','', ''])
				#怪盗紳士 : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
			elif ID == 'KAR_070':
				cond1.append(['battlecry','', ''])
				#イセリアルの売人 : [x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合それらのコストを（2）減らす。
			elif ID == 'KAR_095':
				cond1.append(['battlecry','', ''])
				#動物園ロボ : [x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+1/+1を付与する。
			elif ID == 'KAR_097':
				cond1.append(['battlecry','', ''])
				#ガーディアン・メディヴ : [x]<b>雄叫び:</b>ガーディアンの大杖__アティシュを装備する。
			elif ID == 'KAR_114':
				cond1.append(['battlecry','', ''])
				#バーンズ : <b>雄叫び:</b>自分のデッキのランダムなミニオンの1/1のコピーを[x]1体召喚する。
			elif ID == 'KAR_702':
				cond1.append(['battlecry','', ''])
				#動物園の奇術師 : [x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+2/+2を付与する。
			elif ID == 'KAR_710':
				cond1.append(['battlecry','', ''])
				#魔力細工師 : <b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。
		elif 'LOE_' in ID:
			if ID == 'LOE_011':
				cond1.append(['battlecry','', ''])
				#レノ・ジャクソン : [x]<b>雄叫び:</b>自分のデッキに重複するカードがない場合自分のヒーローの体力を完全に回復する。
			elif ID == 'LOE_019':
				cond1.append(['battlecry','', ''])
				#掘り起こされたラプター : [x]<b>雄叫び:</b> 味方のミニオン1体を選択する。そのミニオンの____<b>断末魔</b>の能力をコピーする。
			elif ID == 'LOE_029':
				cond1.append(['battlecry','', ''])
				#宝飾のスカラベ : [x]<b>雄叫び:</b> コスト3の　カード1枚を<b>発見</b>する。
			elif ID == 'LOE_039':
				cond1.append(['battlecry','', ''])
				#ゴリラロボA-3 : [x]<b>雄叫び:</b>味方に別のメカがいる場合メカ1体を<b>発見</b>する。
			elif ID == 'LOE_047':
				cond1.append(['battlecry','', ''])
				#墓守蜘蛛 : <b>雄叫び:</b> 獣1体を<b>発見</b>する。
			elif ID == 'LOE_073':
				cond1.append(['battlecry','', ''])
				#デビルサウルスの化石 : <b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。
			elif ID == 'LOE_076':
				cond1.append(['battlecry','', ''])
				#サー・フィンレー・マルグルトン : <b>雄叫び:</b>新たな基本ヒーローパワー1つを<b>発見</b>する。
			elif ID == 'LOE_079':
				cond1.append(['battlecry','', ''])
				#エリーズ・スターシーカー : [x]<b>雄叫び:</b> 自分のデッキに「黄金のサルへの地図」1枚を混ぜる。
			elif ID == 'LOE_092':
				cond1.append(['battlecry','', ''])
				#大怪盗ラファーム : <b>雄叫び:</b> 強力な秘宝を1つ<b>発見</b>する。
			elif ID == 'LOE_110':
				cond1.append(['battlecry','', ''])
				#古代のシェード : [x]<b>雄叫び:</b>自分のデッキに「古代の呪い」1枚を混ぜる。「古代の呪い」を引くと_____自分が7ダメージを受ける。
		elif 'LOOT_' in ID:
			if ID == 'LOOT_026':
				cond1.append(['battlecry','', ''])
				#ファルドライ・ストライダー : [x]<b>雄叫び:</b> 自分のデッキに待ち伏せ！3枚を混ぜる。待ち伏せ！を引いた際自分の陣地に4/4のクモを1体召喚する。
			elif ID == 'LOOT_033':
				cond1.append(['battlecry','', ''])
				#大洞窟のキラキラ拾い : [x]<b>雄叫び:</b>自分のデッキから武器を1枚引く。
			elif ID == 'LOOT_069':
				cond1.append(['battlecry','', ''])
				#下水さらい : [x]<b>雄叫び:</b>2/3の「巨大ネズミ」を1体召喚する。
			elif ID == 'LOOT_111':
				cond1.append(['battlecry','', ''])
				#スコーピ・オ・マティック : <b>雄叫び:</b>攻撃力1以下のミニオン1体を破壊する。
			elif ID == 'LOOT_118':
				cond1.append(['battlecry','', ''])
				#漆黒のドラゴン鍛冶 : <b>雄叫び:</b>自分の手札のランダムな武器1つのコストを（2）減らす。
			elif ID == 'LOOT_122':
				cond1.append(['battlecry','', ''])
				#腐蝕ヘドロ : <b>雄叫び:</b>敵の武器を破壊する。
			elif ID == 'LOOT_124':
				cond1.append(['battlecry','', ''])
				#孤高の勇者 : [x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。
			elif ID == 'LOOT_132':
				cond1.append(['battlecry','', ''])
				#ドラゴンスレイヤー : <b>雄叫び:</b>ドラゴン1体に6ダメージを与える。
			elif ID == 'LOOT_150':
				cond1.append(['battlecry','', ''])
				#ファーボルグの苔編み師 : [x]<b>雄叫び:</b>味方のミニオン1体を__6/6のエレメンタルに__変身させる。
			elif ID == 'LOOT_152':
				cond1.append(['battlecry','', ''])
				#賑やかな吟遊詩人 : <b>雄叫び:</b>自身を除く味方のミニオンに体力+1を付与する。
			elif ID == 'LOOT_154':
				cond1.append(['battlecry','', ''])
				#ジャリッパナの騎士 : [x]<b>雄叫び:</b>ランダムなコスト1のミニオン1体を____相手の陣地に召喚する。
			elif ID == 'LOOT_161':
				cond1.append(['battlecry','', ''])
				#肉食キューブ : [x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。
			elif ID == 'LOOT_167':
				cond1.append(['battlecry','', ''])
				#菌術師 : [x]<b>雄叫び:</b>隣接するミニオンに__+2/+2を付与する。
			elif ID == 'LOOT_291':
				cond1.append(['battlecry','', ''])
				#キノコ酒造師 : <b>雄叫び:</b>体力を#4回復する。
			elif ID == 'LOOT_347':
				cond1.append(['battlecry','', ''])
				#コボルトの弟子 : [x]<b>雄叫び:</b>合計3ダメージを敵にランダムに振り分ける。
			elif ID == 'LOOT_357':
				cond1.append(['battlecry','', ''])
				#狐のマリン : [x]<b>雄叫び:</b>相手の陣地に0/8の宝箱を1個召喚する。____<i>(破壊するとお宝入手！)_</i>
			elif ID == 'LOOT_375':
				cond1.append(['battlecry','', ''])
				#ギルド募集係 : <b>雄叫び:</b>コスト（4）以下のミニオンを1体<b>招集</b>する。
			elif ID == 'LOOT_383':
				cond1.append(['battlecry','', ''])
				#飢えているエティン : <b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。
			elif ID == 'LOOT_388':
				cond1.append(['battlecry','', ''])
				#キノコの呪い師 : <b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
			elif ID == 'LOOT_389':
				cond1.append(['battlecry','', ''])
				#クズ拾いのコボルト : <b>雄叫び:</b>自分の破壊された武器1つを自分の手札に戻す。
			elif ID == 'LOOT_516':
				cond1.append(['battlecry','', ''])
				#ゴルゴン・ゾーラ : [x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのゴールデンのコピー1体を自分の手札に追加する。
			elif ID == 'LOOT_521':
				cond1.append(['battlecry','', ''])
				#マスター・オークハート : [x]<b>雄叫び:</b>攻撃力1、2、3のミニオンを1体ずつ<b>招集</b>する。
			elif ID == 'LOOT_526':
				cond1.append(['battlecry','', ''])
				#クライヤミ : [x]最初は<b>休眠状態</b>。<b>雄叫び:</b>_相手のデッキにロウソク3枚を混ぜる。それらが全て引かれるとこれは目覚める。
			elif ID == 'LOOT_529':
				cond1.append(['battlecry','', ''])
				#ヴォイド・リッパー : <b>雄叫び:</b>自身を除く全てのミニオンの攻撃力と体力を入れ替える。
			elif ID == 'LOOT_539':
				cond1.append(['battlecry','', ''])
				#性悪な召喚師 : [x]<b>雄叫び:</b>自分のデッキの呪文を1枚表示する。その呪文と同じコストのランダムな____ミニオン1体を召喚する。
			elif ID == 'LOOT_541':
				cond1.append(['battlecry','', ''])
				#キング・トグワグル : [x]<b>雄叫び:</b>相手とデッキを交換する。再度交換するための身代金の呪文1枚を相手に与える。
		elif 'NEW_' in ID:
			if ID == 'NEW1_014':
				cond1.append(['battlecry','', ''])
				#変装の達人 : <b>雄叫び:</b> 次の自分のターンまで味方のミニオン1体に<b>隠れ身</b>を付与する。
			elif ID == 'NEW1_016':
				cond1.append(['battlecry','', ''])
				#船長のオウム : [x]<b>雄叫び:</b>自分のデッキのランダムな海賊カード1枚を　自分の手札に追加する。
			elif ID == 'NEW1_017':
				cond1.append(['battlecry','', ''])
				#飢えたカニ : <b>雄叫び:</b> マーロック1体を破壊し+2/+2を獲得する。
			elif ID == 'NEW1_018':
				cond1.append(['battlecry','', ''])
				#ブラッドセイルの略奪者 : [x]<b>雄叫び:</b> 自分の武器の攻撃力に等しい攻撃力を　追加で獲得する。
			elif ID == 'NEW1_024':
				cond1.append(['battlecry','', ''])
				#グリーンスキン船長 : [x]<b>雄叫び:</b>自分の武器に__+1/+1を付与する。
			elif ID == 'NEW1_025':
				cond1.append(['battlecry','', ''])
				#ブラッドセイルの海賊 : [x]<b>雄叫び:</b> 敵の武器の耐久度を1減らす。
			elif ID == 'NEW1_029':
				cond1.append(['battlecry','', ''])
				#ミルハウス・マナストーム : <b>雄叫び:</b>  次のターン敵の呪文のコストが（0）になる。
			elif ID == 'NEW1_030':
				cond1.append(['battlecry','', ''])
				#デスウィング : [x]<b>雄叫び:</b> 自身を除く全てのミニオンを破壊し自分の手札を全て破棄する。
			elif ID == 'NEW1_041':
				cond1.append(['battlecry','', ''])
				#暴走コドー : <b>雄叫び:</b> 攻撃力2以下の敵のミニオン1体をランダムに破壊する。
		elif 'OG_' in ID:
			if ID == 'OG_102':
				cond1.append(['battlecry','', ''])
				#闇に説くもの : <b>雄叫び:</b> 味方のミニオン1体と攻撃力・体力を入れ替える。
			elif ID == 'OG_122':
				cond1.append(['battlecry','', ''])
				#峡谷の暴君ムクラ : [x]<b>雄叫び:</b> 「バナナ」2枚を___自分の手札に追加する。
			elif ID == 'OG_131':
				cond1.append(['battlecry','', ''])
				#双皇帝ヴェク＝ロア : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。
			elif ID == 'OG_133':
				cond1.append(['battlecry','', ''])
				#頽廃させしものン＝ゾス : <b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。
			elif ID == 'OG_134':
				cond1.append(['battlecry','', ''])
				#希望の終焉ヨグ＝サロン : [x]<b>雄叫び:</b> この対戦で自分が使用した呪文1回につきランダムな呪文を1つ使用する<i>（対象は_____ランダムに選択される）。_</i>
			elif ID == 'OG_156':
				cond1.append(['battlecry','', ''])
				#マーロックの鯛ド変態 : [x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。
			elif ID == 'OG_161':
				cond1.append(['battlecry','', ''])
				#コールドライトの妖幻者 : <b>雄叫び:</b> マーロックではない全てのミニオンに2ダメージを与える。
			elif ID == 'OG_162':
				cond1.append(['battlecry','', ''])
				#クトゥーンの門弟 : <b>雄叫び:</b> 2ダメージを与える。自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>
			elif ID == 'OG_174':
				cond1.append(['battlecry','', ''])
				#さまよう無貌のもの : [x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。
			elif ID == 'OG_254':
				cond1.append(['battlecry','', ''])
				#秘密を喰らうもの : [x]<b>雄叫び:</b> 敵の<b>秘策</b>全てを破壊する。破壊した秘策1つにつき+1/+1を獲得する。
			elif ID == 'OG_255':
				cond1.append(['battlecry','', ''])
				#破滅の招き手 : <b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>クトゥーンが死亡している場合クトゥーン1枚を自分のデッキに混ぜる。
			elif ID == 'OG_280':
				cond1.append(['battlecry','', ''])
				#クトゥーン : [x]<b>雄叫び:</b>このミニオンの攻撃力に等しい合計ダメージを敵に___ランダムに振り分ける。
			elif ID == 'OG_281':
				cond1.append(['battlecry','', ''])
				#邪悪の誘い手 : [x]<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する<i>___（居場所は問わない）。</i>
			elif ID == 'OG_282':
				cond1.append(['battlecry','', ''])
				#クトゥーンの刃 : [x]<b>雄叫び:</b>ミニオン1体を破壊する。その攻撃力と体力を自分のクトゥーンに追加する<i>（居場所は問わない）。</i>
			elif ID == 'OG_283':
				cond1.append(['battlecry','', ''])
				#クトゥーンに選ばれし者 : [x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>
			elif ID == 'OG_284':
				cond1.append(['battlecry','', ''])
				#黄昏の鎚の地霊術師 : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>
			elif ID == 'OG_291':
				cond1.append(['battlecry','', ''])
				#シャドーキャスター : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンの1/1のコピーを自分の手札に追加する。_____そのカードのコストは（1）。_
			elif ID == 'OG_295':
				cond1.append(['battlecry','', ''])
				#カルトの薬師 : <b>雄叫び:</b>敵のミニオン1体につき自分のヒーローの体力を#2回復する。
			elif ID == 'OG_320':
				cond1.append(['battlecry','', ''])
				#ミッドナイト・ドレイク : <b>雄叫び:</b> このカード以外の自分の手札1枚につき攻撃力+1を獲得する。
			elif ID == 'OG_337':
				cond1.append(['battlecry','', ''])
				#単眼の怪異 : [x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。
			elif ID == 'OG_339':
				cond1.append(['battlecry','', ''])
				#スケラムの狂信者 : [x]<b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する___<i>（居場所は問わない）。</i>_
		elif 'PRO_' in ID:
			if ID == 'PRO_001':
				cond1.append(['battlecry','', ''])
				#エリート・トーレン・チーフテン : <b>雄叫び:</b>  両プレイヤーにロックなパワーあふれるカードを1枚ずつ与える。
		elif 'SCH_' in ID:
			if ID == 'SCH_160':
				cond1.append(['battlecry','', ''])
				#ワンド職人 : [x]<b>雄叫び:</b>自分のクラスのコスト1の呪文1枚を____自分の手札に追加する。
			elif ID == 'SCH_162':
				cond1.append(['battlecry','', ''])
				#ヴェクタス : [x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。
			elif ID == 'SCH_245':
				cond1.append(['battlecry','', ''])
				#筆記の執精 : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。
			elif ID == 'SCH_248':
				cond1.append(['battlecry','', ''])
				#ペン投げ野郎 : [x]<b>雄叫び:</b>1ダメージを与える。<b>魔法活性:</b>___これを自分の手札に戻す。
			elif ID == 'SCH_283':
				cond1.append(['battlecry','', ''])
				#マナ食らいのパンサーラ : [x]<b>雄叫び:</b>このターンに自分がヒーローパワーを使っていた場合カードを1枚引く。
			elif ID == 'SCH_311':
				cond1.append(['battlecry','', ''])
				#空飛ぶほうき : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方のミニオンに<b>急襲</b>を付与する。
			elif ID == 'SCH_312':
				cond1.append(['battlecry','', ''])
				#ツアーガイド : <b>雄叫び:</b>自分が次に使うヒーローパワーのコストは（0）。
			elif ID == 'SCH_351':
				cond1.append(['battlecry','', ''])
				#ジャンディス・バロフ : [x]<b>雄叫び:</b>ランダムなコスト5のミニオン2体を召喚する。2体の内、ダメージを受けると死ぬ1体を秘密裏に選ぶ。
			elif ID == 'SCH_428':
				cond1.append(['battlecry','', ''])
				#伝承守護者ポルケルト : [x]<b>雄叫び:</b>自分のデッキのカードをコストが高い順に並べ替える。
			elif ID == 'SCH_522':
				cond1.append(['battlecry','', ''])
				#スティールダンサー : [x]<b>雄叫び:</b>自分の武器の攻撃力に等しいコストのランダムなミニオンを1体召喚する。
			elif ID == 'SCH_530':
				cond1.append(['battlecry','', ''])
				#代理鏡師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。
			elif ID == 'SCH_713':
				cond1.append(['battlecry','', ''])
				#教団の新入会員 : [x]<b>雄叫び:</b>次のターン、相手の呪文のコストが（1）増える。
		elif 'TRL_' in ID:
			if ID == 'TRL_071':
				cond1.append(['battlecry','', ''])
				#ブラッドセイルの吠猿 : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方の海賊1体につき+1/+1を獲得する。
			elif ID == 'TRL_077':
				cond1.append(['battlecry','', ''])
				#グルバシの盛り上げ屋 : [x]<b>雄叫び:</b><b>雄叫び</b>を持つミニオンの1/1のコピーを1体<b>発見</b>する。そのミニオンのコストは（1）になる。
			elif ID == 'TRL_096':
				cond1.append(['battlecry','', ''])
				#グリフター : <b>雄叫び:</b>カードを2枚<b>発見</b>する。そのうちランダムな1枚を相手に与える。
			elif ID == 'TRL_126':
				cond1.append(['battlecry','', ''])
				#フックタスク船長 : <b>雄叫び:</b>自分のデッキから海賊を3体召喚し_<b>急襲</b>を付与する。
			elif ID == 'TRL_151':
				cond1.append(['battlecry','', ''])
				#元チャンピオン : [x]<b>雄叫び:</b>5/5の「期待の新人」を1体召喚する。
			elif ID == 'TRL_407':
				cond1.append(['battlecry','', ''])
				#給水係 : [x]<b>雄叫び:</b>このターン中に自分が次に使用するヒーローパワーの_コストを（0）にする。
			elif ID == 'TRL_409':
				cond1.append(['battlecry','', ''])
				#サメのロア・グラル : [x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。
			elif ID == 'TRL_504':
				cond1.append(['battlecry','', ''])
				#ブーティ・ベイのノミ屋 : [x]<b>雄叫び:</b>相手に「コイン」1枚を与える。
			elif ID == 'TRL_509':
				cond1.append(['battlecry','', ''])
				#バナナ・バフーン : [x]<b>雄叫び:</b>「バナナ」2枚を___自分の手札に追加する。
			elif ID == 'TRL_512':
				cond1.append(['battlecry','', ''])
				#小ずるい足噛み魔 : [x]<b>生命奪取</b>、<b>雄叫び:</b>__1ダメージを与える。
			elif ID == 'TRL_514':
				cond1.append(['battlecry','', ''])
				#大虎ノーム : [x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。
			elif ID == 'TRL_517':
				cond1.append(['battlecry','', ''])
				#熱狂的闘技場ファン : <b>雄叫び:</b>自分の手札のミニオン全てに+1/+1を付与する。
			elif ID == 'TRL_523':
				cond1.append(['battlecry','', ''])
				#ファイアーツリーの呪術医 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____呪文を1つ<b>発見</b>する。
			elif ID == 'TRL_524':
				cond1.append(['battlecry','heHasTaunt(game)', 'silence'])
				#シールドブレイカー : <b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。
			elif ID == 'TRL_526':
				cond1.append(['battlecry','', ''])
				#ドラゴンモーの爆炎竜 : [x]<b>雄叫び:</b>自身を除く全てのミニオンに______1ダメージを与える。
			elif ID == 'TRL_527':
				cond1.append(['battlecry','', ''])
				#ドラッカリのトリックスター : <b>雄叫び:</b>各プレイヤーは相手のデッキからランダムなカードの__コピーを1枚得る。
			elif ID == 'TRL_530':
				cond1.append(['battlecry','', ''])
				#覆面選手 : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合自分のデッキから___<b>秘策</b>を1つ準備する。
			elif ID == 'TRL_533':
				cond1.append(['battlecry','', ''])
				#アイスクリーム屋 : [x]<b>雄叫び:</b>味方に<b>凍結中</b>のミニオンがいる場合_____装甲を8獲得する。
			elif ID == 'TRL_537':
				cond1.append(['battlecry','', ''])
				#ダ・アンダテイカ : [x]<b>雄叫び:</b>この対戦で死亡した味方のミニオン3体の_____<b>断末魔</b>を獲得する。_
			elif ID == 'TRL_546':
				cond1.append(['battlecry','', ''])
				#凶暴なリクガメ : [x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。
			elif ID == 'TRL_564':
				cond1.append(['battlecry','', ''])
				#モジョー使いジヒィ : <b>雄叫び:</b>各プレイヤーのマナクリスタルを5つにする。
			elif ID == 'TRL_569':
				cond1.append(['battlecry','', ''])
				#ドッカンドラゴン : <b>雄叫び:</b>自分の手札にドラゴンがいる場合敵のミニオン1体に__7ダメージを与える。
		elif 'ULD_' in ID:
			if ID == 'ULD_003':
				cond1.append(['battlecry','', ''])
				#偉大なるゼフリス : <b>雄叫び:</b>自分のデッキに重複するカードがない場合「勝利のカード」の願いを叶える。
			elif ID == 'ULD_157':
				cond1.append(['battlecry','', ''])
				#クエスト中の探検家 : [x]<b>雄叫び:</b>自分が<b>クエスト</b>中の場合__カードを1枚引く。
			elif ID == 'ULD_178':
				cond1.append(['battlecry','', ''])
				#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
			elif ID == 'ULD_186':
				cond1.append(['battlecry','', ''])
				#ファラオの愛猫 : [x]<b>雄叫び:</b><b>蘇り</b>を持つランダムなミニオン1体を自分の__手札に追加する。
			elif ID == 'ULD_188':
				cond1.append(['battlecry','', ''])
				#黄金スカラベ : <b>雄叫び:</b>コスト4のカード1枚を<b>発見</b>する。
			elif ID == 'ULD_189':
				cond1.append(['battlecry','', ''])
				#無貌の潜むもの : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンの体力を2倍にする。
			elif ID == 'ULD_190':
				cond1.append(['battlecry','', ''])
				#ピット・クロコリスク : <b>雄叫び:</b>5ダメージを与える。
			elif ID == 'ULD_191':
				cond1.append(['battlecry','', ''])
				#笑顔の相棒 : [x]<b>雄叫び:</b>味方のミニオン1体に___体力+2を付与する。
			elif ID == 'ULD_196':
				cond1.append(['battlecry','', ''])
				#ネフェルセトの儀式官 : <b>雄叫び:</b>隣接するミニオンの体力を上限まで回復する。
			elif ID == 'ULD_197':
				cond1.append(['battlecry','', ''])
				#流砂のエレメンタル : [x]<b>雄叫び:</b>このターンの間敵のミニオン全てに____攻撃力-2を付与する。
			elif ID == 'ULD_209':
				cond1.append(['battlecry','', ''])
				#ヴァルペラの悪党 : [x]<b>雄叫び:</b>呪文1つを<b>発見</b>するかミステリーチャンスに賭ける。
			elif ID == 'ULD_229':
				cond1.append(['battlecry','', ''])
				#トラブルメーカー : [x]<b>雄叫び:</b>自分のデッキと相手のデッキの一番上の____カードを交換する。
			elif ID == 'ULD_271':
				cond1.append(['battlecry','', ''])
				#傷を負ったトルヴィア : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンに____3ダメージを与える。
			elif ID == 'ULD_288':
				cond1.append(['battlecry','', ''])
				#斂葬のアンカ : [x]<b>雄叫び:</b>自分の手札の<b>断末魔</b>を持つ各ミニオンをそれぞれコスト（1）の1/1に変える。
			elif ID == 'ULD_289':
				cond1.append(['battlecry','', ''])
				#フィッシュフリンガー : [x]<b>雄叫び:</b>各プレイヤーの手札にランダムなマーロック1体を追加する。
			elif ID == 'ULD_304':
				cond1.append(['battlecry','', ''])
				#ファオリス王 : [x]<b>雄叫び:</b>自分の手札の呪文1枚ごとに同コストのランダムな___ミニオンを1体召喚する。
			elif ID == 'ULD_327':
				cond1.append(['battlecry','', ''])
				#バザール強盗 : [x]<b>急襲</b>、<b>雄叫び:</b>他のクラスのランダムなミニオン1体を自分の手札に追加する。
			elif ID == 'ULD_705':
				cond1.append(['battlecry','', ''])
				#魔古の狂信者 : [x]<b>雄叫び:</b>自分の陣地が「魔古の狂信者」で一杯の場合それら全てを生贄にして「大番人ラー」を召喚する。
			elif ID == 'ULD_712':
				cond1.append(['battlecry','', ''])
				#昆虫採集家 : <b>雄叫び:</b><b>急襲</b>を持つ1/1の「イナゴ」を1体召喚する。
			elif ID == 'ULD_719':
				cond1.append(['battlecry','', ''])
				#サバクウサギ : <b>雄叫び:</b>1/1の「サバクウサギ」を2体召喚する。
			elif ID == 'ULD_727':
				cond1.append(['battlecry','', ''])
				#包帯巻き職人 : [x]<b>雄叫び:</b>この対戦で死亡した味方のミニオンを1体<b>発見</b>し、それを自分のデッキに混ぜる。
		elif 'UNG_' in ID:
			if ID == 'UNG_001':
				cond1.append(['battlecry','', ''])
				#プテロダックスのヒナ : <b>雄叫び:</b>___<b>適応</b>する。
			elif ID == 'UNG_002':
				cond1.append(['battlecry','', ''])
				#ヴォルカノサウルス : <b>雄叫び:</b><b>適応</b>し、その後<b>適応</b>する。
			elif ID == 'UNG_009':
				cond1.append(['battlecry','', ''])
				#ラヴァサウルスのチビ : <b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>適応</b>する。
			elif ID == 'UNG_058':
				cond1.append(['battlecry','', ''])
				#レイザーペタル・ラッシャー : [x]<b>雄叫び:</b>「レイザーペタル（1ダメージを与える）」1枚を自分の手札に追加する。
			elif ID == 'UNG_070':
				cond1.append(['battlecry','', ''])
				#トルヴィアのストーンシェイパー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。
			elif ID == 'UNG_072':
				cond1.append(['battlecry','', ''])
				#ストーンヒルの守護者 : [x]<b>挑発</b>、<b>雄叫び:</b><b>挑発</b>を持つミニオン____1体を<b>発見</b>する。
			elif ID == 'UNG_073':
				cond1.append(['battlecry','', ''])
				#ロックプール・ハンター : [x]<b>雄叫び:</b>味方のマーロック1体に+1/+1を付与する。
			elif ID == 'UNG_082':
				cond1.append(['battlecry','', ''])
				#サンダーリザード : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合<b>適応</b>する。
			elif ID == 'UNG_084':
				cond1.append(['battlecry','', ''])
				#ファイアプルーム・フェニックス : <b>雄叫び:</b>2ダメージを与える。
			elif ID == 'UNG_088':
				cond1.append(['battlecry','', ''])
				#トートランの始原術師 : <b>雄叫び:</b>呪文1つを<b>発見</b>しランダムな対象に対して使用する。
			elif ID == 'UNG_089':
				cond1.append(['battlecry','', ''])
				#温厚なメガサウルス : [x]<b>雄叫び:</b>味方のマーロック　全てを<b>適応</b>させる。
			elif ID == 'UNG_099':
				cond1.append(['battlecry','', ''])
				#電撃デビルサウルス : [x]<b>突撃</b>、<b>雄叫び:</b>このターンの間ヒーローを攻撃できない。
			elif ID == 'UNG_113':
				cond1.append(['battlecry','', ''])
				#輝く瞳の斥候 : <b>雄叫び:</b>カードを1枚引く。そのカードのコストを（5）に変える。
			elif ID == 'UNG_205':
				cond1.append(['battlecry','', ''])
				#グレイシャル・シャード : <b>雄叫び:</b>敵1体を<b>凍結</b>させる。
			elif ID == 'UNG_801':
				cond1.append(['battlecry','', ''])
				#巣作りロック鳥 : [x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。
			elif ID == 'UNG_803':
				cond1.append(['battlecry','', ''])
				#エメラルド・リーヴァー : <b>雄叫び:</b>各ヒーローに1ダメージを与える。
			elif ID == 'UNG_807':
				cond1.append(['battlecry','', ''])
				#ゴラッカ・クローラー : [x]<b>雄叫び:</b>海賊1体を破壊し__+1/+1を獲得する。
			elif ID == 'UNG_809':
				cond1.append(['battlecry','', ''])
				#ファイアフライ : <b>雄叫び:</b>1/2のエレメンタル1体を自分の手札に追加する。
			elif ID == 'UNG_816':
				cond1.append(['battlecry','', ''])
				#カリモスの下僕 : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合______エレメンタルを<b>発見</b>する。
			elif ID == 'UNG_840':
				cond1.append(['battlecry','', ''])
				#ジャングルハンター・ヒーメット : [x]<b>雄叫び:</b>自分のデッキのコスト（3）以下の____カードを全て破壊する。
			elif ID == 'UNG_847':
				cond1.append(['battlecry','', ''])
				#ブレイズコーラー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合____5ダメージを与える。
			elif ID == 'UNG_848':
				cond1.append(['battlecry','', ''])
				#始祖ドレイク : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。
			elif ID == 'UNG_851':
				cond1.append(['battlecry','', ''])
				#先遣隊長エリーズ : [x]<b>雄叫び:</b>自分のデッキに未開封の<b>ウンゴロ</b>パック1個を混ぜる。
			elif ID == 'UNG_907':
				cond1.append(['battlecry','', ''])
				#オズラック : [x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。
			elif ID == 'UNG_937':
				cond1.append(['battlecry','', ''])
				#原始フィンの見張り番 : [x]<b>雄叫び:</b>自分の陣地に他のマーロックがいる場合マーロック1体を<b>発見</b>する。
			elif ID == 'UNG_946':
				cond1.append(['battlecry','', ''])
				#暴蝕ウーズ : <b>雄叫び:</b>敵の武器を破壊しその攻撃力に等しい装甲を獲得する。
		elif 'YOD_' in ID:
			if ID == 'YOD_028':
				cond1.append(['battlecry','', ''])
				#スカイダイビングの教官 : [x]<b>雄叫び:</b>自分のデッキからコスト1のミニオンを1体召喚する。
			elif ID == 'YOD_029':
				cond1.append(['battlecry','', ''])
				#ヘイルブリンガー : <b>雄叫び:</b><b>凍結</b>を持つ1/1の「アイス・シャード」を2体召喚する。
			elif ID == 'YOD_030':
				cond1.append(['battlecry','', ''])
				#認可冒険者 : [x]<b>雄叫び:</b>自分が<b>クエスト</b>中の場合自分の手札に「コイン」1枚を追加する。
			elif ID == 'YOD_033':
				cond1.append(['battlecry','', ''])
				#ブームピストル無頼 : [x]<b>雄叫び:</b>次のターン敵の<b>雄叫び</b>を持つカードの__コストが（5）増える。
			elif ID == 'YOD_038':
				cond1.append(['battlecry','', ''])
				#空賊大将クラッグ : [x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。
		pass
	elif '秘策:' in dscrpt:#固有の条件を満たすときに発動
		#基本的にいつでも。内容によっては場との関連がありうる。
		if ID == 'BT_042':
			cond1.append(['secret','', ''])
			#偽装 : <b>秘策:</b>味方のミニオンが攻撃された時、それをコストが（3）高いランダムなミニオンに変身させる。
		elif ID == 'BT_707':
			cond1.append(['secret','', ''])
			#伏兵 : <b>秘策:</b>相手がミニオンを手札から使用した後<b>猛毒</b>を持つ2/3の伏兵を1体召喚する。
		elif ID == 'BT_709':
			cond1.append(['secret','', ''])
			#汚い手 : [x]<b>秘策:</b>相手が呪文を使用した後カードを2枚引く。
		elif ID == 'LOOT_204':
			cond1.append(['secret','', ''])
			#九死一生 : <b>秘策:</b>味方のミニオンが死亡した時、そのミニオン1体を自分の手札に戻す。そのコストは（2）減る。
		elif ID == 'LOOT_210':
			cond1.append(['secret','', ''])
			#突然の裏切り : <b>秘策:</b>ミニオンが自分のヒーローを攻撃した時、代わりにそのミニオンに隣接する誰かを攻撃する。
		elif ID == 'LOOT_214':
			cond1.append(['secret','', ''])
			#雲隠れ : <b>秘策:</b>自分のヒーローがダメージを受けた後このターンの間<b>無敵</b>になる。
		elif ID == 'SCH_706':
			cond1.append(['secret','', ''])
			#カンニング : [x]<b>秘策:</b>相手のターンの終了時相手がそのターンに手札から使用した全てのカードのコピーを自分の手札に追加する。

	if '<b>挑発</b>' in dscrpt:
		#このカードが挑発カードの場合
		#→味方の場に出ているカードが多いときはGO
		#挑発を付与するタイプの呪文の場合
		#→付与する対象のミニオンがある場合にはGO
		if ID == 'AT_017':
			cond1.append(['taunt','haveDragon(game)', ''])
			#トワイライトの守護者 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。
		elif ID == 'AT_097':
			cond1.append(['taunt','', ''])
			#トーナメント参加者 : <b>挑発</b>
		elif ID == 'AT_112':
			cond1.append(['taunt','', ''])
			#槍試合の名手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。
		elif ID == 'AT_114':
			cond1.append(['taunt','', ''])
			#邪悪なる野次馬 : <b>挑発</b>
		elif ID == 'AT_123':
			cond1.append(['taunt','', ''])
			#チルモー : [x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。
		elif ID == 'BOT_021':
			cond1.append(['taunt','', ''])
			#ブロンズ・ゲートキーパー : <b>超電磁</b><b>挑発</b>
		elif ID == 'BOT_050':
			cond1.append(['taunt','', ''])
			#錆びついたリサイクラー : <b>挑発</b><b>生命奪取</b>
		elif ID == 'BOT_270':
			cond1.append(['taunt','', ''])
			#含み笑う発明家 : [x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。
		elif ID == 'BOT_296':
			cond1.append(['taunt','', ''])
			#オメガ・ディフェンダー : [x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_
		elif ID == 'BOT_448':
			cond1.append(['taunt','', ''])
			#損傷したステゴトロン : <b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。
		elif ID == 'BOT_548':
			cond1.append(['taunt','', ''])
			#ジリアックス : <b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>
		elif ID == 'BT_155':
			cond1.append(['taunt','', ''])
			#屑鉄山のコロッサス : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。
		elif ID == 'BT_715':
			cond1.append(['taunt','', ''])
			#ボーンチューワーの喧嘩屋 : <b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。
		elif ID == 'BT_716':
			cond1.append(['taunt','', ''])
			#ボーンチューワーの前衛 : <b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。
		elif ID == 'BT_720':
			cond1.append(['taunt','', ''])
			#錆鉄騎の略奪者 : <b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。
		elif ID == 'BT_730':
			cond1.append(['taunt','', ''])
			#大物気取りのオーク : <b>挑発</b>体力が最大の場合このミニオンは____攻撃力+2を得る。
		elif ID == 'CFM_652':
			cond1.append(['taunt','', ''])
			#二流の強面 : [x]<b>挑発</b>相手の陣地に3体以上のミニオンがいる場合_____コストが（2）減る。
		elif ID == 'CFM_653':
			cond1.append(['taunt','', ''])
			#日雇い護衛 : <b>挑発</b>
		elif ID == 'CFM_688':
			cond1.append(['taunt','', ''])
			#トゲ付きのホグライダー : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。
		elif ID == 'CFM_790':
			cond1.append(['taunt','', ''])
			#ドブネズミ : [x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。
		elif ID == 'CFM_806':
			cond1.append(['taunt','', ''])
			#ラシオン : [x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。
		elif ID == 'CFM_854':
			cond1.append(['taunt','', ''])
			#満開の古代樹 : <b>挑発</b>
		elif ID == 'CS1_042':
			cond1.append(['taunt','', ''])
			#ゴールドシャイアの歩兵 : <b>挑発</b>
		elif ID == 'CS1_069':
			cond1.append(['taunt','', ''])
			#フェン・クリーパー : <b>挑発</b>
		elif ID == 'CS2_121':
			cond1.append(['taunt','', ''])
			#フロストウルフの兵卒 : <b>挑発</b>
		elif ID == 'CS2_125':
			cond1.append(['taunt','', ''])
			#鉄毛のグリズリー : <b>挑発</b>
		elif ID == 'CS2_127':
			cond1.append(['taunt','', ''])
			#シルバーバックの長 : <b>挑発</b>
		elif ID == 'CS2_162':
			cond1.append(['taunt','', ''])
			#闘技場の覇者 : <b>挑発</b>
		elif ID == 'CS2_179':
			cond1.append(['taunt','', ''])
			#センジン・シールドマスタ : <b>挑発</b>
		elif ID == 'CS2_187':
			cond1.append(['taunt','', ''])
			#ブーティ・ベイのボディガード : <b>挑発</b>
		elif ID == 'DAL_058':
			cond1.append(['taunt','', ''])
			#ヤジロボ : <b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。
		elif ID == 'DAL_088':
			cond1.append(['taunt','', ''])
			#金庫番 : <b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。
		elif ID == 'DAL_096':
			cond1.append(['taunt','', ''])
			#ヴァイオレット監獄の看守 : <b>挑発</b><b>呪文ダメージ+1</b>
		elif ID == 'DAL_551':
			cond1.append(['taunt','', ''])
			#誇り高き守護者 : [x]<b>挑発</b>味方に他のミニオンがいない場合__攻撃力+2を得る。
		elif ID == 'DAL_560':
			cond1.append(['taunt','', ''])
			#酒場のヒロイック女将 : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_
		elif ID == 'DAL_775':
			cond1.append(['taunt','', ''])
			#トンネル爆破係 : [x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。
		elif ID == 'DRG_064':
			cond1.append(['taunt','', ''])
			#ズルドラクの儀式官 : [x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__
		elif ID == 'DRG_065':
			cond1.append(['taunt','', ''])
			#ヒポグリフ : <b>急襲</b>、<b>挑発</b>
		elif ID == 'DRG_242':
			cond1.append(['taunt','', ''])
			#ガラクロンドの盾 : <b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
		elif ID == 'EX1_002':
			cond1.append(['taunt','', ''])
			#黒騎士 : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。
		elif ID == 'EX1_032':
			cond1.append(['taunt','', ''])
			#サンウォーカー : [x]<b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'EX1_058':
			cond1.append(['taunt','', ''])
			#サンフューリーの護衛 : [x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。
		elif ID == 'EX1_093':
			cond1.append(['taunt','', ''])
			#アルガスの守護者 : <b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。
		elif ID == 'EX1_097':
			cond1.append(['taunt','', ''])
			#涜れしもの : [x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。
		elif ID == 'EX1_390':
			cond1.append(['taunt','', ''])
			#トーレン・ウォリアー : [x]<b>挑発</b>ダメージを受けている間は___攻撃力+3を得る。
		elif ID == 'EX1_396':
			cond1.append(['taunt','', ''])
			#魔古山の番兵 : <b>挑発</b>
		elif ID == 'EX1_405':
			cond1.append(['taunt','', ''])
			#盾持ち : <b>挑発</b>
		elif ID == 'FP1_012':
			cond1.append(['taunt','', ''])
			#ヘドロゲッパー : [x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。
		elif ID == 'FP1_024':
			cond1.append(['taunt','', ''])
			#不安定なグール : [x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。
		elif ID == 'GIL_120':
			cond1.append(['taunt','', ''])
			#怒れるエティン : <b>挑発</b>
		elif ID == 'GIL_207':
			cond1.append(['taunt','', ''])
			#幽霊民兵 : <b>木霊</b>、<b>挑発</b>
		elif ID == 'GIL_526':
			cond1.append(['taunt','', ''])
			#ワームガード : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。
		elif ID == 'GIL_527':
			cond1.append(['taunt','', ''])
			#フェルソウルの異端審問官 : <b>生命奪取</b>、<b>挑発</b>
		elif ID == 'GIL_623':
			cond1.append(['taunt','', ''])
			#ウィッチウッドのグリズリー : [x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。
		elif ID == 'GIL_667':
			cond1.append(['taunt','', ''])
			#朽ちかけたアップルバウム : [x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。
		elif ID == 'GIL_809':
			cond1.append(['taunt','', ''])
			#眠るスチームロボ : <b>挑発</b>
		elif ID == 'GVG_085':
			cond1.append(['taunt','', ''])
			#マジウザ・オ・トロン : <b>挑発</b><b>聖なる盾</b>
		elif ID == 'GVG_093':
			cond1.append(['taunt','', ''])
			#ターゲット・ダミー : <b>挑発</b>
		elif ID == 'GVG_097':
			cond1.append(['taunt','', ''])
			#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
		elif ID == 'GVG_098':
			cond1.append(['taunt','', ''])
			#ノームレガン歩兵 : [x]<b>突撃</b>、<b>挑発</b>
		elif ID == 'GVG_107':
			cond1.append(['taunt','', ''])
			#エンハンス・オ・メカーノ : <b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>
		elif ID == 'ICC_314':
			cond1.append(['taunt','', ''])
			#リッチキング : [x]<b>挑発</b>自分のターンの終了時ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。
		elif ID == 'ICC_466':
			cond1.append(['taunt','', ''])
			#サロナイト鉱山の奴隷 : [x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。
		elif ID == 'ICC_705':
			cond1.append(['taunt','', ''])
			#ボーンメア : [x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。
		elif ID == 'ICC_853':
			cond1.append(['taunt','', ''])
			#ヴァラナール公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。
		elif ID == 'ICC_912':
			cond1.append(['taunt','', ''])
			#躯の駆り手 : [x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。
		elif ID == 'KAR_011':
			cond1.append(['taunt','', ''])
			#気取り屋の俳優 : <b>挑発</b>
		elif ID == 'KAR_037':
			cond1.append(['taunt','', ''])
			#番鳥 : <b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。
		elif ID == 'KAR_061':
			cond1.append(['taunt','', ''])
			#キュレーター : [x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。
		elif ID == 'KAR_710':
			cond1.append(['taunt','', ''])
			#魔力細工師 : <b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。
		elif ID == 'LOE_073':
			cond1.append(['taunt','', ''])
			#デビルサウルスの化石 : <b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。
		elif ID == 'LOOT_117':
			cond1.append(['taunt','', ''])
			#蝋のエレメンタル : <b>挑発</b><b>聖なる盾</b>
		elif ID == 'LOOT_124':
			cond1.append(['taunt','', ''])
			#孤高の勇者 : [x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。
		elif ID == 'LOOT_131':
			cond1.append(['taunt','', ''])
			#グリーン・ジェリー : [x]自分のターンの終了時<b>挑発</b>を持つ1/2のウーズを1体召喚する。
		elif ID == 'LOOT_137':
			cond1.append(['taunt','', ''])
			#眠れるドラゴン : <b>挑発</b>
		elif ID == 'LOOT_315':
			cond1.append(['taunt','', ''])
			#トログのキノコ食い : [x]<b>挑発</b>、<b>猛毒</b>
		elif ID == 'LOOT_383':
			cond1.append(['taunt','', ''])
			#飢えているエティン : <b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。
		elif ID == 'NEW1_022':
			cond1.append(['taunt','', ''])
			#悪辣なる海賊 : [x]<b>挑発</b>自分の武器の攻撃力1につき_____コストが（1）減る。
		elif ID == 'NEW1_040':
			cond1.append(['taunt','', ''])
			#ホガー : [x]自分のターンの終了時<b>挑発</b>を持つ2/2のノールを1体召喚する。
		elif ID == 'OG_131':
			cond1.append(['taunt','', ''])
			#双皇帝ヴェク＝ロア : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。
		elif ID == 'OG_145':
			cond1.append(['taunt','', ''])
			#マジヤバ・オ・トロン : <b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'OG_153':
			cond1.append(['taunt','', ''])
			#変・クリーパー : <b>挑発</b>
		elif ID == 'OG_156':
			cond1.append(['taunt','', ''])
			#マーロックの鯛ド変態 : [x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。
		elif ID == 'OG_174':
			cond1.append(['taunt','', ''])
			#さまよう無貌のもの : [x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。
		elif ID == 'OG_249':
			cond1.append(['taunt','', ''])
			#蝕まれしトーレン : [x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。
		elif ID == 'OG_284':
			cond1.append(['taunt','', ''])
			#黄昏の鎚の地霊術師 : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>
		elif ID == 'OG_318':
			cond1.append(['taunt','', ''])
			#エルウィンの変災ホガー : [x]このミニオンがダメージを受ける度<b>挑発</b>を持つ2/2の　ノールを1体召喚する。
		elif ID == 'OG_327':
			cond1.append(['taunt','', ''])
			#のたうつ触手 : <b>挑発</b>
		elif ID == 'OG_337':
			cond1.append(['taunt','', ''])
			#単眼の怪異 : [x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。
		elif ID == 'SCH_232':
			cond1.append(['taunt','', ''])
			#クリムゾンの竜学生 : [x]<b>魔法活性:</b>攻撃力+1と<b>挑発</b>を獲得する。
		elif ID == 'SCH_709':
			cond1.append(['taunt','', ''])
			#イキってる四年生 : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。
		elif ID == 'SCH_710':
			cond1.append(['taunt','', ''])
			#往餓術師 : [x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。
		elif ID == 'TRL_363':
			cond1.append(['taunt','', ''])
			#サロナイト鉱山の奴隷監督 : [x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。
		elif ID == 'TRL_513':
			cond1.append(['taunt','', ''])
			#モッシュオグの審判 : <b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'TRL_514':
			cond1.append(['taunt','', ''])
			#大虎ノーム : [x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。
		elif ID == 'TRL_515':
			cond1.append(['taunt','', ''])
			#会場警備係 : [x]<b>挑発</b>敵のミニオン1体につきコストが（1）減る。
		elif ID == 'TRL_524':
			cond1.append(['taunt','heHasTaunt(game)', 'silence'])
			#シールドブレイカー : <b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。
		elif ID == 'TRL_550':
			cond1.append(['taunt','', ''])
			#アマニの戦熊 : <b>急襲</b>、<b>挑発</b>
		elif ID == 'ULD_178':
			cond1.append(['taunt','', ''])
			#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
		elif ID == 'ULD_179':
			cond1.append(['taunt','', ''])
			#ファランクス指揮官 : [x]味方の<b>挑発</b>を持つミニオン全ては攻撃力+2を得る。
		elif ID == 'ULD_189':
			cond1.append(['taunt','', ''])
			#無貌の潜むもの : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンの体力を2倍にする。
		elif ID == 'ULD_193':
			cond1.append(['taunt','', ''])
			#動くモニュメント : <b>挑発</b>
		elif ID == 'ULD_198':
			cond1.append(['taunt','', ''])
			#うつろう蜃気楼 : [x]<b>挑発</b>自分のターンの開始時このミニオンを____自分のデッキに混ぜる。
		elif ID == 'ULD_208':
			cond1.append(['taunt','', ''])
			#カルトゥートの守護者 : [x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。
		elif ID == 'ULD_215':
			cond1.append(['taunt','', ''])
			#包帯ゴーレム : [x]<b>蘇り</b>自分のターンの終了時<b>挑発</b>を持つ1/1の「スカラベ」を1体召喚する。
		elif ID == 'ULD_250':
			cond1.append(['taunt','', ''])
			#虫食いゴブリン : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。
		elif ID == 'ULD_271':
			cond1.append(['taunt','', ''])
			#傷を負ったトルヴィア : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンに____3ダメージを与える。
		elif ID == 'ULD_275':
			cond1.append(['taunt','', ''])
			#ボーン・レイス : <b>挑発</b>、<b>蘇り</b>
		elif ID == 'UNG_070':
			cond1.append(['taunt','', ''])
			#トルヴィアのストーンシェイパー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。
		elif ID == 'UNG_071':
			cond1.append(['taunt','', ''])
			#巨大マストドン : <b>挑発</b>
		elif ID == 'UNG_072':
			cond1.append(['taunt','', ''])
			#ストーンヒルの守護者 : [x]<b>挑発</b>、<b>雄叫び:</b><b>挑発</b>を持つミニオン____1体を<b>発見</b>する。
		elif ID == 'UNG_801':
			cond1.append(['taunt','', ''])
			#巣作りロック鳥 : [x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。
		elif ID == 'UNG_808':
			cond1.append(['taunt','', ''])
			#不屈のカタツムリ : [x]<b>挑発</b>、<b>猛毒</b>
		elif ID == 'UNG_810':
			cond1.append(['taunt','', ''])
			#ステゴドン : <b>挑発</b>
		elif ID == 'UNG_848':
			cond1.append(['taunt','', ''])
			#始祖ドレイク : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。
		elif ID == 'UNG_907':
			cond1.append(['taunt','', ''])
			#オズラック : [x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。
		elif ID == 'UNG_928':
			cond1.append(['taunt','', ''])
			#タール・クリーパー : [x]<b>挑発</b>相手のターン中は___攻撃力+2を得る。
		elif ID == 'YOD_038':
			cond1.append(['taunt','', ''])
			#空賊大将クラッグ : [x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。
	if '聖なる盾' in dscrpt:#一回の攻撃を受けない
		if ID == 'AT_087':
			cond1.append(['divineShield','', ''])
			#アージェントの騎兵 : <b>突撃:</b><b>聖なる盾</b>
		elif ID == 'AT_095':
			cond1.append(['divineShield','', ''])
			#静寂の騎士 : <b>隠れ身</b><b>聖なる盾</b>
		elif ID == 'AT_112':
			cond1.append(['divineShield','', ''])
			#槍試合の名手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。
		elif ID == 'AT_129':
			cond1.append(['divineShield','', ''])
			#フィヨラ・ライトベイン : <b>自分</b>がこのミニオンに対して呪文を使用する度<b>聖なる盾</b>を獲得する。
		elif ID == 'BOT_270':
			cond1.append(['divineShield','', ''])
			#含み笑う発明家 : [x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。
		elif ID == 'BOT_414':
			cond1.append(['divineShield','', ''])
			#クロークスケイルの化学者 : <b>隠れ身</b><b>聖なる盾</b>
		elif ID == 'BOT_534':
			cond1.append(['divineShield','', ''])
			#ブル・ドーザー : <b>聖なる盾</b>
		elif ID == 'BOT_548':
			cond1.append(['divineShield','', ''])
			#ジリアックス : <b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>
		elif ID == 'BT_722':
			cond1.append(['divineShield','', ''])
			#ガーディアン改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>聖なる盾</b>を付与する。_
		elif ID == 'DAL_078':
			cond1.append(['divineShield','', ''])
			#旅の治療師 : <b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。
		elif ID == 'DAL_085':
			cond1.append(['divineShield','', ''])
			#ダララン・クルセイダー : <b>聖なる盾</b>
		elif ID == 'DRG_079':
			cond1.append(['divineShield','', ''])
			#躱し身のワーム : <b>聖なる盾</b>、<b>急襲</b>呪文とヒーローパワーの標的にならない。
		elif ID == 'EX1_008':
			cond1.append(['divineShield','', ''])
			#アージェントの従騎士 : <b>聖なる盾</b>
		elif ID == 'EX1_020':
			cond1.append(['divineShield','', ''])
			#スカーレット・クルセイダー : <b>聖なる盾</b>
		elif ID == 'EX1_023':
			cond1.append(['divineShield','', ''])
			#シルバームーンの守護兵 : <b>聖なる盾</b>
		elif ID == 'EX1_032':
			cond1.append(['divineShield','', ''])
			#サンウォーカー : [x]<b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'EX1_067':
			cond1.append(['divineShield','', ''])
			#アージェントの司令官 : [x]<b>突撃</b>、<b>聖なる盾</b>
		elif ID == 'EX1_590':
			cond1.append(['divineShield','', ''])
			#ブラッドナイト : [x]<b>雄叫び:</b> 全てのミニオンは<b>聖なる盾</b>を失う。失われた聖なる盾1つにつき+3/+3を獲得する。
		elif ID == 'GIL_202':
			cond1.append(['divineShield','', ''])
			#ギルニーアスの近衛兵 : [x]<b>聖なる盾</b>、<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
		elif ID == 'GVG_079':
			cond1.append(['divineShield','', ''])
			#フォース・タンクMAX : <b>聖なる盾</b>
		elif ID == 'GVG_085':
			cond1.append(['divineShield','', ''])
			#マジウザ・オ・トロン : <b>挑発</b><b>聖なる盾</b>
		elif ID == 'GVG_107':
			cond1.append(['divineShield','', ''])
			#エンハンス・オ・メカーノ : <b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>
		elif ID == 'ICC_912':
			cond1.append(['divineShield','', ''])
			#躯の駆り手 : [x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。
		elif ID == 'ICC_913':
			cond1.append(['divineShield','', ''])
			#穢れし狂信者 : <b>聖なる盾</b><b>呪文ダメージ+1</b>
		elif ID == 'LOOT_117':
			cond1.append(['divineShield','', ''])
			#蝋のエレメンタル : <b>挑発</b><b>聖なる盾</b>
		elif ID == 'LOOT_124':
			cond1.append(['divineShield','', ''])
			#孤高の勇者 : [x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。
		elif ID == 'LOOT_125':
			cond1.append(['divineShield','', ''])
			#石肌のバジリスク : <b>聖なる盾</b><b>猛毒</b>
		elif ID == 'OG_145':
			cond1.append(['divineShield','', ''])
			#マジヤバ・オ・トロン : <b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'OG_283':
			cond1.append(['divineShield','', ''])
			#クトゥーンに選ばれし者 : [x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>
		elif ID == 'SCH_143':
			cond1.append(['divineShield','', ''])
			#聖レイジャー : <b>聖なる盾</b>
		elif ID == 'TRL_513':
			cond1.append(['divineShield','', ''])
			#モッシュオグの審判 : <b>挑発</b>、<b>聖なる盾</b>
		elif ID == 'ULD_178':
			cond1.append(['divineShield','', ''])
			#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
		elif ID == 'ULD_721':
			cond1.append(['divineShield','', ''])
			#月の巨像 : <b>聖なる盾</b>、<b>蘇り</b>
		elif ID == 'UNG_070':
			cond1.append(['divineShield','', ''])
			#トルヴィアのストーンシェイパー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。

	if '隠れ身' in dscrpt:#こちらから攻撃するまでの攻撃対象にならない
		if ID == 'AT_095':
			cond1.append(['stealth','', ''])
			#静寂の騎士 : <b>隠れ身</b><b>聖なる盾</b>
		elif ID == 'BOT_414':
			cond1.append(['stealth','', ''])
			#クロークスケイルの化学者 : <b>隠れ身</b><b>聖なる盾</b>
		elif ID == 'BOT_555':
			cond1.append(['stealth','', ''])
			#先遣者セレスティア : [x]<b>隠れ身</b>相手がミニオンを手札から使用した後そのミニオンの_コピーになる。
		elif ID == 'BOT_562':
			cond1.append(['stealth','', ''])
			#カッパーテイルモドキ : [x]<b>雄叫び:</b>次の自分のターンまで__<b>隠れ身</b>を獲得する。
		elif ID == 'BT_701':
			cond1.append(['stealth','', ''])
			#スパイミストレス : <b>隠れ身</b>
		elif ID == 'BT_702':
			cond1.append(['stealth','', ''])
			#アッシュタン・スレイヤー : [x]<b>雄叫び:</b><b>隠れ身</b>状態のミニオン1体にこのターンの間、攻撃力+3と<b>無敵</b>を付与する。
		elif ID == 'BT_703':
			cond1.append(['stealth','', ''])
			#呪われた流れ者 : [x]<b>断末魔:</b><b>隠れ身</b>を持つ7/5の影を1体召喚する。
		elif ID == 'BT_710':
			cond1.append(['stealth','', ''])
			#グレイハート族の賢者 : [x]<b>雄叫び:</b>味方に<b>隠れ身</b>状態のミニオンがいる場合______カードを2枚引く。__
		elif ID == 'BT_713':
			cond1.append(['stealth','', ''])
			#アカマ : [x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。
		elif ID == 'BT_717':
			cond1.append(['stealth','', ''])
			#穴掘りスコーピッド : [x]<b>雄叫び:</b>2ダメージを与える。これにより対象が死んだ場合<b>隠れ身</b>を獲得する。
		elif ID == 'CFM_344':
			cond1.append(['stealth','', ''])
			#飛刀手流忍者・六丸 : [x]<b>隠れ身</b>このミニオンの攻撃でミニオンが 死亡した時、自分のデッキからマーロックを2体召喚する。
		elif ID == 'CFM_634':
			cond1.append(['stealth','', ''])
			#蓮華凶手 : [x]<b>隠れ身</b>このミニオンが攻撃してミニオンを倒す度に　<b>隠れ身</b>を獲得する。
		elif ID == 'CFM_636':
			cond1.append(['stealth','', ''])
			#シャドウ・レイジャー : <b>隠れ身</b>
		elif ID == 'CFM_656':
			cond1.append(['stealth','', ''])
			#裏街の探偵 : <b>雄叫び:</b> 敵のミニオンは<b>隠れ身</b>を失う。
		elif ID == 'CFM_691':
			cond1.append(['stealth','', ''])
			#翡翠の鎌刀 : [x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
		elif ID == 'CFM_694':
			cond1.append(['stealth','', ''])
			#影の師匠 : [x]<b>雄叫び:</b><b>隠れ身</b>を持つミニオン1体に　+2/+2を付与する。
		elif ID == 'CFM_781':
			cond1.append(['stealth','', ''])
			#蒐集家シャク : [x]<b>隠れ身</b>このミニオンが攻撃する度相手のクラスのランダムなカード1枚を自分の手札に追加する。
		elif ID == 'CS2_161':
			cond1.append(['stealth','', ''])
			#レイヴンホルトの暗殺者 : <b>隠れ身</b>
		elif ID == 'DAL_090':
			cond1.append(['stealth','', ''])
			#ヘンチ・クランの隠密 : <b>隠れ身</b>
		elif ID == 'DRG_074':
			cond1.append(['stealth','', ''])
			#擬装した飛行船 : [x]<b>雄叫び:</b>次の自分のターンまで自身を除く味方のメカに<b>隠れ身</b>を付与する。
		elif ID == 'EX1_010':
			cond1.append(['stealth','', ''])
			#ウォーゲンのスパイ : <b>隠れ身</b>
		elif ID == 'EX1_017':
			cond1.append(['stealth','', ''])
			#ジャングル・パンサー : <b>隠れ身</b>
		elif ID == 'EX1_028':
			cond1.append(['stealth','', ''])
			#ストラングルソーントラ : <b>隠れ身</b>
		elif ID == 'EX1_128':
			cond1.append(['stealth','', ''])
			#隠蔽 : [x]次の自分のターンまで味方のミニオン全てに<b>隠れ身</b>を付与する。
		elif ID == 'EX1_522':
			cond1.append(['stealth','', ''])
			#埋伏の暗殺者 : [x]<b>隠れ身</b>、<b>猛毒</b>
		elif ID == 'FP1_005':
			cond1.append(['stealth','', ''])
			#ナクスラーマスの亡霊 : <b>隠れ身:</b> 自分のターンの開始時+1/+1を獲得する。
		elif ID == 'GVG_025':
			cond1.append(['stealth','', ''])
			#隻眼のチート : [x]自分が海賊を召喚する度、<b>隠れ身</b>を獲得する。
		elif ID == 'GVG_081':
			cond1.append(['stealth','', ''])
			#ギルブリン・ストーカー : <b>隠れ身</b>
		elif ID == 'GVG_088':
			cond1.append(['stealth','', ''])
			#オーガ・ニンジャ : <b>隠れ身:</b>50%の確率で、指定していない敵を攻撃する。
		elif ID == 'GVG_109':
			cond1.append(['stealth','', ''])
			#ミニ・メイジ : [x]<b>呪文ダメージ+1</b><b>隠れ身</b>
		elif ID == 'KAR_044':
			cond1.append(['stealth','', ''])
			#モローズ : [x]<b>隠れ身</b>自分のターンの終了時1/1の家令を1体召喚する。
		elif ID == 'LOOT_136':
			cond1.append(['stealth','', ''])
			#潜む悪鬼 : <b>隠れ身</b>自身を除く味方のミニオンは攻撃力+1を得る。
		elif ID == 'NEW1_014':
			cond1.append(['stealth','', ''])
			#変装の達人 : <b>雄叫び:</b> 次の自分のターンまで味方のミニオン1体に<b>隠れ身</b>を付与する。
		elif ID == 'OG_247':
			cond1.append(['stealth','', ''])
			#ウォーゲン変異体 : <b>隠れ身</b>
		elif ID == 'SCH_234':
			cond1.append(['stealth','', ''])
			#偽善系の二年生 : [x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。
		elif ID == 'SCH_426':
			cond1.append(['stealth','', ''])
			#潜入者リリアン : [x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。
		elif ID == 'SCH_708':
			cond1.append(['stealth','', ''])
			#日陰草の非行生徒 : [x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。
		elif ID == 'TRL_010':
			cond1.append(['stealth','', ''])
			#ハーフタイムの清掃員 : [x]<b>隠れ身</b>、<b>血祭:</b>___装甲を3獲得する。
		elif ID == 'TRL_092':
			cond1.append(['stealth','', ''])
			#サメの精霊 : [x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。
		elif ID == 'ULD_274':
			cond1.append(['stealth','', ''])
			#荒れ地の暗殺者 : <b>隠れ身</b>、<b>蘇り</b>
		elif ID == 'UNG_812':
			cond1.append(['stealth','', ''])
			#サーベルストーカー : <b>隠れ身</b>
		elif ID == 'UNG_814':
			cond1.append(['stealth','', ''])
			#巨大スズメバチ : [x]<b>隠れ身</b>、<b>猛毒</b>
		elif ID == 'YOD_006':
			cond1.append(['stealth','', ''])
			#脱走したマナセイバー : [x]<b>隠れ身</b>これが攻撃する度このターンの間のみマナクリスタルを1つ獲得する。
		elif ID == 'YOD_016':
			cond1.append(['stealth','', ''])
			#飛掠船員 : <b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。

	if '呪文ダメージ' in dscrpt:
		#攻撃呪文カードを持っていたら+2
		if ID == 'AT_093':
			cond1.append(['spellDamage','', ''])
			#極寒のスノボルト : <b>呪文ダメージ+1</b>
		elif ID == 'AT_117':
			cond1.append(['spellDamage','', ''])
			#司会者 : <b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。
		elif ID == 'BT_008':
			cond1.append(['spellDamage','', ''])
			#錆鉄の入門者 : [x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。
		elif ID == 'BT_724':
			cond1.append(['spellDamage','', ''])
			#イセリアル改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'CFM_039':
			cond1.append(['spellDamage','', ''])
			#路上のトリックスター : <b>呪文ダメージ+1</b>
		elif ID == 'CS2_142':
			cond1.append(['spellDamage','', ''])
			#コボルトの地霊術師 : <b>呪文ダメージ+1</b>
		elif ID == 'CS2_155':
			cond1.append(['spellDamage','', ''])
			#大魔術師 : <b>呪文ダメージ+1</b>
		elif ID == 'CS2_197':
			cond1.append(['spellDamage','', ''])
			#オーガのメイジ達 : <b>呪文ダメージ+1</b>
		elif ID == 'DAL_089':
			cond1.append(['spellDamage','', ''])
			#呪文書綴じ師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。
		elif ID == 'DAL_096':
			cond1.append(['spellDamage','', ''])
			#ヴァイオレット監獄の看守 : <b>挑発</b><b>呪文ダメージ+1</b>
		elif ID == 'DAL_434':
			cond1.append(['spellDamage','', ''])
			#魔力の番人 : [x]自分が<b>呪文ダメージ</b>を持っていない限り攻撃できない。
		elif ID == 'DAL_548':
			cond1.append(['spellDamage','', ''])
			#アゼライト・エレメンタル : [x]自分のターンの開始時<b>呪文ダメージ+2</b>を得る。
		elif ID == 'DAL_748':
			cond1.append(['spellDamage','', ''])
			#マナタンク : <b>呪文ダメージ+1</b>
		elif ID == 'EX1_012':
			cond1.append(['spellDamage','', ''])
			#ブラッドメイジ・サルノス : [x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。
		elif ID == 'EX1_284':
			cond1.append(['spellDamage','', ''])
			#アジュア・ドレイク : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。
		elif ID == 'EX1_563':
			cond1.append(['spellDamage','', ''])
			#マリゴス : <b>呪文ダメージ+5</b>
		elif ID == 'EX1_582':
			cond1.append(['spellDamage','', ''])
			#ダラランのメイジ : <b>呪文ダメージ+1</b>
		elif ID == 'EX1_584':
			cond1.append(['spellDamage','', ''])
			#老練のメイジ : [x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'GIL_121':
			cond1.append(['spellDamage','', ''])
			#ダークマイア・ムーンキン : <b>呪文ダメージ+2</b>
		elif ID == 'GIL_529':
			cond1.append(['spellDamage','', ''])
			#スペルシフター : [x]<b>呪文ダメージ+1</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
		elif ID == 'GVG_109':
			cond1.append(['spellDamage','', ''])
			#ミニ・メイジ : [x]<b>呪文ダメージ+1</b><b>隠れ身</b>
		elif ID == 'ICC_093':
			cond1.append(['spellDamage','', ''])
			#タスカーの漁師 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'ICC_856':
			cond1.append(['spellDamage','', ''])
			#スペルウィーヴァー : <b>呪文ダメージ+2</b>
		elif ID == 'ICC_913':
			cond1.append(['spellDamage','', ''])
			#穢れし狂信者 : <b>聖なる盾</b><b>呪文ダメージ+1</b>
		elif ID == 'OG_082':
			cond1.append(['spellDamage','', ''])
			#コボルトの地霊呪痛死 : <b>呪文ダメージ+2</b>
		elif ID == 'SCH_245':
			cond1.append(['spellDamage','', ''])
			#筆記の執精 : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。
		elif ID == 'SCH_270':
			cond1.append(['spellDamage','', ''])
			#根源学の予習 : [x]<b>呪文ダメージ</b>を持つミニオンを1体<b>発見</b>する。自分が次に使用する<b>呪文ダメージ</b>を持つミニオンのコストが（1）減る。
		elif ID == 'SCH_273':
			cond1.append(['spellDamage','', ''])
			#ラス・フロストウィスパー : [x]自分のターンの終了時全ての敵に$1ダメージを与える<i>（<b>呪文ダメージ</b>によって__強化される）</i>。
		elif ID == 'SCH_530':
			cond1.append(['spellDamage','', ''])
			#代理鏡師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。
		elif ID == 'TRL_312':
			cond1.append(['spellDamage','', ''])
			#強仙師 : ダメージを受けている間は<b>呪文ダメージ+2</b>を得る。
	if '<b>猛毒</b>' in dscrpt:
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
#キャラクターが回復を受ける度

#自分が_呪文を使う度
#相手が呪文を使う度
#自分がカードを引く度
#相手がカードを引く度
#このカードが自分の手札にある間
#<b>雄叫び</b>を持つカードを使う度
#<b>雄叫び</b>を持つミニオンを召喚する度
#自分がカードをデッキに混ぜる度
#<b>秘策</b>が使用される度

#プレイヤーが呪文を使う度
#自分がマーロックを召喚する度
#ミニオンを召喚する度
#カードを手札から使用する度
#自分がミニオンを引く度
#カードを手札から使用__する度
#相手がカードを使う度
#自分が海賊を召喚する度
#ミニオンを場に出す度
#味方のメカが死ぬ度
#敵のミニオンが死ぬ度
#自分の武器が破壊される度
#味方のミニオンが死ぬ度

#ミニオンを手札から使用する度
#ミニオンが死ぬ度
#自分が獣を引く度
#手札から呪文が使用される度
#隣接するミニオンがダメージを受ける度
#自分のヒーローの体力を3以上回復する度
#自分が<b>コンボ</b>カードを手札から使用する度


############# 場合 #########################

	if 'ドラゴン' in dscrpt:
		if ID == 'AT_017':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[AT_017][トワイライトの守護者]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。)
		if ID == 'AT_123':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[AT_123][チルモー]([x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。)
		if ID == 'BRM_029':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[BRM_029][レンド・ブラックハンド]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合<b>レジェンド</b>ミニオン1体を破壊する。)
		if ID == 'BRM_033':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[BRM_033][ブラックウィングの技術者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合____+1/+1を獲得する。)
		if ID == 'BRM_034':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[BRM_034][ブラックウィングの変性者]([x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合_____3ダメージを与える。)
		if ID == 'DRG_072':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[DRG_072][スカイフィン](<b>雄叫び:</b>自分の手札にドラゴンがいる場合ランダムなマーロックを2体召喚する。)
		if ID == 'DRG_081':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[DRG_081][スケイルライダー]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____2ダメージを与える。)
		if ID == 'GIL_526':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[GIL_526][ワームガード]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。)
		if ID == 'KAR_033':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[KAR_033][ブック・ワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力3以下の敵の______ミニオン1体を破壊する。_)
		if ID == 'GIL_601':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[GIL_601][スケイルワーム]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。)
		if ID == 'KAR_062':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[KAR_062][ネザースパイトの歴史家]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合____ドラゴン1体を<b>発見</b>する。)
		if ID == 'TRL_523':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[TRL_523][ファイアーツリーの呪術医]([x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____呪文を1つ<b>発見</b>する。)
		if ID == 'TRL_569':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[TRL_569][ドッカンドラゴン](<b>雄叫び:</b>自分の手札にドラゴンがいる場合敵のミニオン1体に__7ダメージを与える。)
		if ID == 'DRG_063':
			if haveDragon(game):
				cond1.append(['dragon','' ,''])
			pass
			#[DRG_063][ドラゴンモーの密猟者](<b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。)
		if ID == 'DRG_089':
			if haveNoDuplicate(game):
				cond1.append(['dragon','' ,''])
			pass
			#[DRG_089][竜の女王アレクストラーザ]([x]<b>雄叫び:</b>_自分のデッキに重複するカードがない場合


############### キーワード #####################	
	if 'コンボ' in dscrpt:
		if player.combo:
			pass
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


def haveDragon(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.DRAGON:
			return True
	return False

def noDeck(game):
   player = game.current_player
   return len(player.deck)==0

def noHand(game):
   player = game.current_player
   return len(player.hand)==0

def noCharacter(game):
   player = game.current_player
   return len(player.characters)==0


