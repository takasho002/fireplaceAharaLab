def RogueCat_condition_devineShield(game,ID):
	myCondition=[]
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
	return myCondition

def RogueCat_condition_stealth(game,ID):
	myCondition=[]
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
	return myCondition

def RogueCat_condition_spellDamage(game,ID):
	myCondition=[]
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
	return myCondition