# agent_RogueCat.py

import random

from hearthstone.enums import CardClass, CardType, Race
from utils import ExceptionPlay, Candidate, executeAction, getCandidates
from agent_Standard import postAction

from agent_RogueCat_1 import *
from agent_RogueCat_2 import *
from agent_RogueCat_3 import *
from agent_RogueCat_4 import *
from agent_RogueCat_5 import *


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
		if ('カードを使う' in dscrpt or '召喚する' in dscrpt or '場に出す' in dscrpt or '使用する' in dscrpt or 'ミニオンがいる' in dscrpt) and '<b>' not in dscrpt:
			print("		elif ID  == '%s':"%(card.id))
			print("			myCondition.append(['playCard','', ''])")
			print("			#%s : %s"%(card.name, card.description.replace('\n','')))
	return collection

def RogueCatAI(game, option=[], debugLog=False):
	while True:
		player = game.current_player
		myCandidate = getCandidates(game)
		if len(myCandidate)>0:
			if debugLog:
				print( '--------------------------')
				for n in range(len(myCandidate)):
					card = myCandidate[n].card
					target = myCandidate[n].target
					myC = RogueCat_Condition(game, card, target)
					print("%r %s : %s"%(card.id, card.data.name, card.data.description.replace('\n','')))
					print("->%r"%target)
					for repeat in range(len(myC)):
						print("%s"%myC[repeat])
				print( '--------------------------')
			myChoice = random.choice(myCandidate)
			executeAction(game, myChoice, debugLog=debugLog)
			postAction(player)
		else:
			return

def haveDragon(game):
	return False



def RogueCat_Condition(game, card, target) -> list:
	myCondition=[]#満たしている条件
	cond2=[]#効果
	dscrpt = card.data.description.replace('\n','')
	player = game.current_player
	myHeroHealth=player.hero.health
	hisHeroHealth=player.opponent.hero.health
	myTauntH = 0
	myMinionH = 0
	myAttack = 0
	for cd in player.characters:
		if cd.can_attack():
			myAttack += cd.atk
		if cd.taunt:
			myTauntH += cd.health
		if cd.type == CardType.MINION:
			myMinionH += cd.health
	hisTauntH = 0
	hisAttack = 0
	for cd in player.opponent.characters:
		if cd.can_attack():
			hisAttack += cd.atk
		if cd. taunt:
			hisTauntH += cd.health
	myHeroRemainder=myHeroHealth+myTauntH-hisAttack
	hisHeroRemainder=hisHeroHealth+hisTauntH-myAttack
	myMinionRemainder=myMinionH
	ID = card.id
	if card.type==CardType.HERO:
		return myCondition
	if '激励' in dscrpt:#ヒーローパワーを使うと発動する
		#基本的にいつでもあとまわし。内容によっては場との関連がありうる。
		pass
	if '突撃' in dscrpt:# card.charge:#突撃
		if ID == 'AT_070':
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'lessConst'])
		elif ID in {'AT_125', 'UNG_099'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'noAttack'])
		elif ID in {'EX1_116'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'summon'])
		elif ID in {'CS2_146'}:
			if player.hero.weapon != None:
				myCondition.append(['charge', 'myRemainder<hisRemainder', None])
		elif ID in {'CS2_124', 'AT_087', 'CS2_131', 'CS2_171', 'CS2_213', 'EX1_062', 'EX1_067', 'GVG_098'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', None])
		pass
	if '断末魔:' in dscrpt:#card.has_deathrattle:#断末魔
		myCondition.extend( RogueCat_condition_deathrattle(game,ID))
	if '雄叫び:' in dscrpt:#card.has_battlecry:#雄叫び
		myCondition.extend(RogueCat_condition_battlecry(game,ID))
	if '秘策:' in dscrpt:
		myCondition.extend(RogueCat_condition_secret(game,ID))
	if '<b>挑発</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_taunt(game,ID))
	if '聖なる盾' in dscrpt:#一回の攻撃を受けない
		myCondition.extend(RogueCat_condition_devineShield(game,ID))
	if '隠れ身' in dscrpt:#こちらから攻撃するまでの攻撃対象にならない
		myCondition.extend(RogueCat_condition_stealth(game,ID))
	if '呪文ダメージ' in dscrpt:
		myCondition.extend(RogueCat_condition_spellDamage(game,ID))
	if '<b>猛毒</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_poisonous(game,ID))
		pass
	if '<b>超電磁</b>' in dscrpt:
		#<b>超電磁</b>
		pass
	if '<b>急襲</b>' in dscrpt:
		#<b>急襲</b>
		myCondition.extend(RogueCat_condition_rush(game,ID))
	if '<b>生命奪取</b>' in dscrpt:
		#<b>生命奪取</b>
		myCondition.append(['lifeSteal','',''])
		pass
	if '<b>休眠状態</b>' in dscrpt:
		#<b>休眠状態</b>
		myCondition.append(['asleep','',''])
		pass
	if '<b>発見</b>' in dscrpt:
		#<b>発見</b>
		myCondition.append(['discover','',''])
		pass
	if '魔法活性' in dscrpt:#Spellburst
		myCondition.append(['spellBurst','',''])
		pass
########### 度 #################

	if ID=='CFM_325':
		if haveWeapon(game):
			myCondition.append(['weapon','','help'])
			#[CFM_325][ちんけなバッカニーア]([x]自分のヒーローが武器を装備している場合攻撃力+2を得る。)
	elif ID=='NEW1_027':
		if havePirate(game):
			myCondition.append(['pirate','','help'])
			#[NEW1_027][南海の船長](自身を除く味方の海賊は+1/+1を得る。)
	elif ID=='TRL_127':
		if havePirate(game):
			myCondition.append(['pirate','','damage'])
		#[TRL_127][大砲連射]([x]ランダムな敵1体に$3ダメージを与える。味方の海賊1体につき1回これを繰り返す。)




############### コンボ #####################	
	if 'コンボ' in dscrpt:
		if player.combo:
			myCondition.append(['combo','',''])
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
#[ULD_285][鉤付きシミター](<b>コンボ:</b>攻撃力+2を獲得する。)
#[UNG_063][カミツキソウ](<b>コンボ:</b> このターン中で先に使用されたカード1枚につき+1/+1を獲得する。)
#[UNG_064][ヴァイルスパイン・スレイヤー](<b>コンボ:</b>ミニオン1体を破壊する。)
#[YOD_017][影の彫刻家]([x]<b>コンボ:</b>このターン中に先に使用されたカード1枚につきカードを1枚引く。)

#使わない
#[BOT_447][結晶術師]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_)
#[TRL_546][凶暴なリクガメ]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。)
#[UNG_087][ビタータイド・ヒドラ](このミニオンがダメージを受ける度自分のヒーローに___3ダメージを与える。)

#####カード
#自分がカードをデッキに混ぜる度
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がカードを引く度
#相手がカードを引く度
#このカードが自分の手札にある間
#<b>秘策</b>が使用される度
#カードを手札から使用する度
#自分がミニオンを引く度
#カードを手札から使用__する度
#相手がカードを使う度
#自分が獣を引く度
#自分のデッキに重複するカードがない場合
#自分の手札にドラゴンがいる場合
#自分のデッキに重複するカードがない場合
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がミニオンを手札から使用する度

#####召喚
#<b>雄叫び</b>を持つカードを使う度
#<b>雄叫び</b>を持つミニオンを召喚する度
#自分がマーロックを召喚する度
#ミニオンを場に出す度
#ミニオンを召喚する度
#自分が海賊を召喚する度
#ミニオンを手札から使用する度
#味方に体力6以上のミニオンがいる場合
#相手の陣地に3体以上のミニオンがいる場合
#このミニオンを除いて味方に2体以上のミニオンがいる場合
	if ('カードを使う' in dscrpt or '召喚する' in dscrpt or '場に出す' in dscrpt or '使用する' in dscrpt or 'ミニオンがいる' in dscrpt):
		if ID  == 'AT_035':
			myCondition.append(['playCard','', ''])
			#土蜘蛛 : [x]相手のデッキに「待ち伏せ！」3枚を混ぜる。「待ち伏せ！」が引かれた際自分の陣地に4/4の_____ネルビアンを1体召喚する。
		elif ID  == 'BOT_280':
			myCondition.append(['playCard','', ''])
			#幻像術師 : [x]相手がミニオンを手札から使用した後そのミニオンの1/1のコピーを1体召喚する。
		elif ID  == 'BRM_019':
			myCondition.append(['playCard','', ''])
			#ぐったりガブ呑み亭の常連 : [x]このミニオンがダメージを受けて生き延びた後「ぐったりガブ呑み亭の常連」をもう1体召喚する。
		elif ID  == 'BRM_022':
			myCondition.append(['playCard','', ''])
			#ドラゴンの卵 : このミニオンがダメージを受ける度2/1のチビドラゴン1体を召喚する。
		elif ID  == 'BT_255':
			myCondition.append(['playCard','', ''])
			#ケルサス・サンストライダー : [x]毎ターン、自分が使用する呪文のコストは3回目ごとに（0）になる。
		elif ID  == 'BT_721':
			myCondition.append(['playCard','', ''])
			#飛び散る腐汁 : [x]自分のターンの終了時このミニオンと同じ攻撃力・体力の腐汁を1体召喚する。
		elif ID  == 'CFM_637':
			myCondition.append(['playCard','', ''])
			#海賊パッチーズ : [x]自分が海賊を手札から使用した後自分のデッキからこの____ミニオンを召喚する。
		elif ID  == 'DAL_550':
			myCondition.append(['playCard','', ''])
			#最下層ウーズ : [x]このミニオンがダメージを受けて生き延びた後このミニオンのコピーを1体召喚する。
		elif ID  == 'DAL_553':
			myCondition.append(['playCard','', ''])
			#悪い大噛み魔術師 : [x]自分のターンの終了時ランダムなコスト6のミニオン1体を召喚する。
		elif ID  == 'DAL_558':
			myCondition.append(['playCard','', ''])
			#大魔術師ヴァルゴス : [x]自分のターンの終了時自分がこのターンに使用した呪文1つを再使用する。<i>（対象はランダム）</i>
		elif ID  == 'DAL_774':
			myCondition.append(['playCard','', ''])
			#異境の乗騎売り : [x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。
		elif ID  == 'DRG_056':
			myCondition.append(['playCard','', ''])
			#パラシュート・パイレート : [x]自分が海賊を手札から使用した後自分の手札から____このミニオンを召喚する。
		elif ID  == 'DRG_091':
			myCondition.append(['playCard','', ''])
			#シュ＝マ : [x]自分のターンの終了時自分の陣地に1/1の「触手」を可能な限り召喚する。
		elif ID  == 'EX1_076':
			myCondition.append(['playCard','', ''])
			#ポケットサイズの召喚師 : 毎ターン最初に手札から使用するミニオンのコストが（1）減る。
		elif ID  == 'EX1_145':
			myCondition.append(['playCard','', ''])
			#段取り : [x]このターン自分が次に使用する呪文のコストが（2）減る。
		elif ID  == 'EX1_509':
			myCondition.append(['playCard','', ''])
			#マーロックのタイドコーラー : [x]自分がマーロックを召喚する度___攻撃力+1を獲得する。
		elif ID  == 'EX1_597':
			myCondition.append(['playCard','', ''])
			#インプ使い : [x]自分のターンの終了時このミニオンに1ダメージを与え1/1のインプを1体召喚する。
		elif ID  == 'EX1_614':
			myCondition.append(['playCard','', ''])
			#ザヴィウス : [x]自分がカードを手札から使用した後2/1のサテュロスを1体召喚する。
		elif ID  == 'FP1_013':
			myCondition.append(['playCard','', ''])
			#ケルスザード : [x]各ターンの終了時そのターンに死亡した味方のミニオン全てを召喚する。
		elif ID  == 'GIL_620':
			myCondition.append(['playCard','', ''])
			#人形師ドリアン : [x]自分がミニオンを引く度、そのミニオンの1/1のコピーを1体召喚する。
		elif ID  == 'GVG_016':
			myCondition.append(['playCard','', ''])
			#フェル・リーヴァー : 相手がカードを使う度自分のデッキの上から3枚のカードを捨てる。
		elif ID  == 'GVG_104':
			myCondition.append(['playCard','', ''])
			#ホブゴブリン : [x]自分が攻撃力1のミニオンを場に出す度そのミニオンに______+2/+2を付与する。
		elif ID  == 'GVG_116':
			myCondition.append(['playCard','', ''])
			#メカジニア・サーマプラッグ : 敵のミニオンが死ぬ度に、レプラノームを1体召喚する。
		elif ID  == 'GVG_118':
			myCondition.append(['playCard','', ''])
			#アーシネイター・トログザー : 相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。
		elif ID  == 'ICC_900':
			myCondition.append(['playCard','', ''])
			#壊死のガイスト : [x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。
		elif ID  == 'ICC_911':
			myCondition.append(['playCard','', ''])
			#号泣のバンシー : [x]自分がカードを使う度自分のデッキの上から3枚のカードを除去する。
		elif ID  == 'LOE_053':
			myCondition.append(['playCard','', ''])
			#西風のジニー : [x]自分がこのミニオンを除く、味方のミニオンに呪文を使用した後、その呪文をコピーし、このミニオンに対して使用する。
		elif ID  == 'LOE_086':
			myCondition.append(['playCard','', ''])
			#召喚石 : 自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。
		elif ID  == 'LOE_107':
			myCondition.append(['playCard','', ''])
			#不気味な像 : [x]戦場に他のミニオンがいると攻撃できない。
		elif ID  == 'LOOT_394':
			myCondition.append(['playCard','', ''])
			#ワメキノコ : [x]自分のターンの終了時ランダムなコスト1のミニオン1体を召喚する。
		elif ID  == 'LOOT_414':
			myCondition.append(['playCard','', ''])
			#記録保管大臣 : [x]自分のターンの終了時自分のデッキにある呪文1つを使用する。<i>__（対象はランダムに選択）</i>
		elif ID  == 'NEW1_026':
			myCondition.append(['playCard','', ''])
			#ヴァイオレット・アイの講師 : [x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。
		elif ID  == 'SCH_537':
			myCondition.append(['playCard','', ''])
			#魔術のトーテム : [x]自分のターンの終了時コスト（3）以下のランダムな呪文を1つ使用する。
		elif ID  == 'TRL_507':
			myCondition.append(['playCard','', ''])
			#シャークフィンのファン : [x]自分のヒーローが攻撃した後1/1の海賊を1体召喚する。
		elif ID  == 'ULD_286':
			myCondition.append(['playCard','', ''])
			#死の影 : [x]ミニオン1体を選択する。引かれた際そのコピー1体を召喚する「影」3枚を自分のデッキに混ぜる。
		elif ID  == 'ULD_290':
			myCondition.append(['playCard','', ''])
			#歴史愛好家 : [x]自分がミニオンを手札から使用する度自分の手札のランダムなミニオン1体に+1/+1を付与する。
		elif ID  == 'UNG_843':
			myCondition.append(['playCard','', ''])
			#ヴォラックス : 自分がこのミニオンに呪文を使用した後1/1の植物を1体召喚し呪文のコピーをその植物に対して使用する。
		pass

#####体力など
#自分のヒーローの体力を3以上回復する度
#キャラクターが回復を受ける度
#自分のヒーローがダメージを受ける度
#このミニオンがダメージを受ける度
#隣接するミニオンがダメージを受ける度
#自分のヒーローの体力を3以上回復する度
#ダメージを受けている間

#####装備
#自分が武器を装備する度
	if '武器' in dscrpt:
		if ID  == 'AT_029':
			myCondition.append(['weapon','', ''])
			#バッカニーア : 自分が武器を装備する度、その武器に攻撃力+1を付与する。
		elif ID  == 'AT_034':
			myCondition.append(['weapon','', ''])
			#毒仕込みの刃 : 自分のヒーローパワーはこの武器と置き換わる代わりに、この武器に攻撃力+1を付与する。
		elif ID  == 'CFM_325':
			myCondition.append(['weapon','', ''])
			#ちんけなバッカニーア : [x]自分のヒーローが武器を装備している場合攻撃力+2を得る。
		elif ID  == 'CS2_074':
			myCondition.append(['weapon','', ''])
			#致死毒 : 自分の武器に攻撃力+2を付与する。
		elif ID  == 'CS2_233':
			myCondition.append(['weapon','', ''])
			#千刃乱舞 : 自分の武器を破壊しその攻撃力に等しいダメージを敵のミニオン全てに与える。
		elif ID  == 'GVG_022':
			myCondition.append(['weapon','', ''])
			#ティンカーの刃研ぎ油 : 自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。
		elif ID  == 'SCH_519':
			myCondition.append(['weapon','', ''])
			#ヴァルペラの毒刃研究者 : 自分の武器は攻撃力+2を得る。
		elif ID  == 'SCH_623':
			myCondition.append(['weapon','', ''])
			#斧刀講 : [x]カードを2枚引く。自分の武器の攻撃力1につきコストが（1）減る。


#####攻撃
#ヒーローを攻撃する度
#このミニオンが攻撃してミニオンを倒す度
#このミニオンが攻撃する度
#味方のミニオンが攻撃された時

#####呪文
	if '呪文' in dscrpt:
		if ID  == 'AT_129':
			myCondition.append(['spell','', ''])
			#フィヨラ・ライトベイン : <b>自分</b>がこのミニオンに対して呪文を使用する度<b>聖なる盾</b>を獲得する。
		elif ID  == 'AT_131':
			myCondition.append(['spell','', ''])
			#エイディス・ダークベイン : [x]<b>自分</b>がこのミニオンに対して呪文を使用する度ランダムな敵に_____3ダメージを与える。
		elif ID  == 'BOT_098':
			myCondition.append(['spell','', ''])
			#パワー切れのモーラー : [x]このターンに自分が呪文を使用した___場合のみ攻撃できる。
		elif ID  == 'BRM_020':
			myCondition.append(['spell','', ''])
			#ドラゴンキン・ソーサラー : [x]<b>自分</b>がこのミニオンに対して呪文を使用する度+1/+1を獲得する。
		elif ID  == 'BT_709':
			myCondition.append(['spell','', ''])
			#汚い手 : [x]<b>秘策:</b>相手が呪文を使用した後カードを2枚引く。
		elif ID  == 'CFM_060':
			myCondition.append(['spell','', ''])
			#レッド・マナ・ワーム : [x]自分が呪文を使う度攻撃力+2を獲得する。
		elif ID  == 'CFM_669':
			myCondition.append(['spell','', ''])
			#強盗ログ : [x]相手が呪文を使う度自分の手札に「コイン」1枚を追加する。
		elif ID  == 'CFM_807':
			myCondition.append(['spell','', ''])
			#競売王ビアードオ : [x]自分が呪文を使用した後自分のヒーローパワーを再度使用可能にする。
		elif ID  == 'DAL_774':
			myCondition.append(['spell','', ''])
			#異境の乗騎売り : [x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。
		elif ID  == 'EX1_055':
			myCondition.append(['spell','', ''])
			#マナ中毒者 : [x]自分が呪文を使う度そのターンの間攻撃力+2を獲得する。
		elif ID  == 'EX1_095':
			myCondition.append(['spell','', ''])
			#ガジェッツァンの競売人 : 自分が呪文を使う度カードを1枚引く。
		elif ID  == 'EX1_100':
			myCondition.append(['spell','', ''])
			#探話士チョー : プレイヤーが呪文を使う度、もう1人のプレイヤーの手札にその呪文のコピーを追加する。
		elif ID  == 'EX1_187':
			myCondition.append(['spell','', ''])
			#魔力喰らい : [x]自分が呪文を使う度+2/+2を獲得する。
		elif ID  == 'GVG_028':
			myCondition.append(['spell','', ''])
			#商大公ガリーウィックス : [x]相手が呪文を使う度自分はその呪文のコピー1枚を獲得し、相手は「ガリーウィックスの______コイン」1枚を獲得する。_
		elif ID  == 'GVG_067':
			myCondition.append(['spell','', ''])
			#ストーンスプリンター・トログ : [x]相手が呪文を使う度攻撃力+1を獲得する。
		elif ID  == 'GVG_068':
			myCondition.append(['spell','', ''])
			#バーリー・ロックジョー・トログ : [x]相手が呪文を使う度攻撃力+2を獲得する。
		elif ID  == 'GVG_118':
			myCondition.append(['spell','', ''])
			#アーシネイター・トログザー : 相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。
		elif ID  == 'ICC_201':
			myCondition.append(['spell','', ''])
			#骰は投げられた : [x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。
		elif ID  == 'KAR_036':
			myCondition.append(['spell','', ''])
			#魔力異常体 : [x]自分が呪文を使う度このミニオンに体力+1を付与する。
		elif ID  == 'LOE_053':
			myCondition.append(['spell','', ''])
			#西風のジニー : [x]自分がこのミニオンを除く、味方のミニオンに呪文を使用した後、その呪文をコピーし、このミニオンに対して使用する。
		elif ID  == 'LOE_086':
			myCondition.append(['spell','', ''])
			#召喚石 : 自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。
		elif ID  == 'LOOT_130':
			myCondition.append(['spell','', ''])
			#魔力の暴帝 : [x]このターンにコスト（5）以上の呪文を使用していた場合コスト（0）。
		elif ID  == 'NEW1_020':
			myCondition.append(['spell','', ''])
			#熱狂する火霊術師 : [x]自分が呪文を使用した後全てのミニオンに1ダメージを与える。
		elif ID  == 'NEW1_026':
			myCondition.append(['spell','', ''])
			#ヴァイオレット・アイの講師 : [x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。
		elif ID  == 'SCH_157':
			myCondition.append(['spell','', ''])
			#魔法の大釜 : [x]<b>魔法活性:</b>使われた呪文と同コストのランダムな呪文を使用する。
		elif ID  == 'SCH_710':
			myCondition.append(['spell','', ''])
			#往餓術師 : [x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。
		elif ID  == 'SCH_714':
			myCondition.append(['spell','', ''])
			#英才エレク : [x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
		elif ID  == 'UNG_843':
			myCondition.append(['spell','', ''])
			#ヴォラックス : 自分がこのミニオンに呪文を使用した後1/1の植物を1体召喚し呪文のコピーをその植物に対して使用する。

#####死去
	if '死' in dscrpt:
		if ID  == 'CFM_658':
			myCondition.append(['death','', ''])
			#奥部屋の用心棒 : [x]味方のミニオンが死ぬ度、攻撃力+1を獲得する。
		elif ID  == 'GVG_106':
			myCondition.append(['death','', ''])
			#ジャンクロボ : [x]味方のメカが死ぬ度+2/+2を獲得する。
		elif ID  == 'GVG_116':
			myCondition.append(['death','', ''])
			#メカジニア・サーマプラッグ : 敵のミニオンが死ぬ度に、レプラノームを1体召喚する。
		elif ID  == 'ICC_900':
			myCondition.append(['death','', ''])
			#壊死のガイスト : [x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。
		elif ID  == 'LOOT_149':
			myCondition.append(['death','', ''])
			#回廊漁り蟲 : [x]このカードが手札にある間ミニオンが死ぬ度コストが（1）減る。
		elif ID  == 'tt_004':
			myCondition.append(['death','', ''])
			#屍肉喰いのグール : [x]ミニオンが死ぬ度攻撃力+1を獲得する。

#####ターン
#自分のターンの終了時
#自分のターンの終了時
#このターンの間のみ
#自分のターンの終了時
#このターンの間
#自分のターンの開始時







	return myCondition


def haveBeast(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.BEAST:
			return True
	return False

def haveDeathrattle(game):
	player = game.current_player
	for card in player.hand:
		if card.has_deathrattle:
			return True
	return False

def haveDragon(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.DRAGON:
			return True
	return False

def haveMechanical(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.MECHANICAL:
			return True
	return False

def haveMinion(game):
	return onMinion(game)

def havePirate(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.PIRATE:
			return True
	return False

def haveSecret(game):
	player = game.current_player
	if len(player.secrets)>0:
		return True
	return False

def haveWeapon(game):
	return onWeapon(game)

def noDeck(game):
	player = game.current_player
	return len(player.deck)==0

def noHand(game):
	player = game.current_player
	return len(player.hand)==0

def noCharacter(game):
   player = game.current_player
   return len(player.characters)==0

def heHasMinion(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.type == CardType.MINION:
			return True
	return False

def heHasDemon(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.race == Race.DEMON:
			return True
	return False

def heHasDeathrattle(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.has_deathrattle:
			return True
	return False

def heHasNonVanilla(game):
	player = game.current_player.opponent
	for card in player.field:
		if len(card.data.descrption)>=3:
			return True
	return False

def heHasTaunt(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.taunt:
			return True
	return False

def haveNoDuplicate(game):
	player = game.current_player
	for card1 in player.field:
		for card2 in player.field:
			if card1!=card2 and card1.name==card2.name:
				return True
	return False

def OnMechanical(game):
	player = game.current_player
	for card in player.field:
		if card.race == Race.MECHANICAL:
			return True
	return False

def onMinion(game):
	player = game.current_player
	for card in player.field:
		if card.type == CardType.MINION:
			return True
	return False

def onPirate(game):
	player = game.current_player
	for card in player.field:
		if card.race == Race.PIRATE:
			return True
	return False

def onWeapon(game):
	player = game.current_player
	for card in player.field:
		if card.type == CardType.WEAPON:
			return True
	return False
