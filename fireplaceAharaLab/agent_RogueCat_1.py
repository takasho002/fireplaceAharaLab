def RogueCat_condition_deathrattle(game):
	cond1=[]
	#if card.has_deathrattle:
	#断末魔　死ぬときに発動 deathrattle
	#発動のタイミングが相手に依存しているので、基本的にいつでも。
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
			cond1.append(['','haveDeathrattle(game)', ''])
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
	return cond1