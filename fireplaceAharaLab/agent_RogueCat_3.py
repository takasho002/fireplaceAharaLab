def RogueCat_condition_secret(game,ID):
	myCondition=[]
	#固有の条件を満たすときに発動
	#基本的にいつでも。内容によっては場との関連がありうる。
	if ID == 'BT_042':
		myCondition.append(['secret','', ''])
		#偽装 : <b>秘策:</b>味方のミニオンが攻撃された時、それをコストが（3）高いランダムなミニオンに変身させる。
	elif ID == 'BT_707':
		myCondition.append(['secret','', ''])
		#伏兵 : <b>秘策:</b>相手がミニオンを手札から使用した後<b>猛毒</b>を持つ2/3の伏兵を1体召喚する。
	elif ID == 'BT_709':
		myCondition.append(['secret','', ''])
		#汚い手 : [x]<b>秘策:</b>相手が呪文を使用した後カードを2枚引く。
	elif ID == 'LOOT_204':
		myCondition.append(['secret','', ''])
		#九死一生 : <b>秘策:</b>味方のミニオンが死亡した時、そのミニオン1体を自分の手札に戻す。そのコストは（2）減る。
	elif ID == 'LOOT_210':
		myCondition.append(['secret','', ''])
		#突然の裏切り : <b>秘策:</b>ミニオンが自分のヒーローを攻撃した時、代わりにそのミニオンに隣接する誰かを攻撃する。
	elif ID == 'LOOT_214':
		myCondition.append(['secret','', ''])
		#雲隠れ : <b>秘策:</b>自分のヒーローがダメージを受けた後このターンの間<b>無敵</b>になる。
	elif ID == 'SCH_706':
		myCondition.append(['secret','', ''])
		#カンニング : [x]<b>秘策:</b>相手のターンの終了時相手がそのターンに手札から使用した全てのカードのコピーを自分の手札に追加する。
	return myCondition


def RogueCat_condition_taunt(game,ID):
	myCondition=[]
	#このカードが挑発カードの場合
	#→味方の場に出ているカードが多いときはGO
	#挑発を付与するタイプの呪文の場合
	#→付与する対象のミニオンがある場合にはGO
	if ID == 'AT_017':
		myCondition.append(['taunt','haveDragon(game)', ''])
		#トワイライトの守護者 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。
	elif ID == 'AT_097':
		myCondition.append(['taunt','', ''])
		#トーナメント参加者 : <b>挑発</b>
	elif ID == 'AT_112':
		myCondition.append(['taunt','', ''])
		#槍試合の名手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。
	elif ID == 'AT_114':
		myCondition.append(['taunt','', ''])
		#邪悪なる野次馬 : <b>挑発</b>
	elif ID == 'AT_123':
		myCondition.append(['taunt','', ''])
		#チルモー : [x]<b>挑発</b>、<b>断末魔:</b>自分の手札にドラゴンがいる場合、全てのミニオンに3ダメージを与える。
	elif ID == 'BOT_021':
		myCondition.append(['taunt','', ''])
		#ブロンズ・ゲートキーパー : <b>超電磁</b><b>挑発</b>
	elif ID == 'BOT_050':
		myCondition.append(['taunt','', ''])
		#錆びついたリサイクラー : <b>挑発</b><b>生命奪取</b>
	elif ID == 'BOT_270':
		myCondition.append(['taunt','', ''])
		#含み笑う発明家 : [x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。
	elif ID == 'BOT_296':
		myCondition.append(['taunt','', ''])
		#オメガ・ディフェンダー : [x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_
	elif ID == 'BOT_448':
		myCondition.append(['taunt','', ''])
		#損傷したステゴトロン : <b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。
	elif ID == 'BOT_548':
		myCondition.append(['taunt','', ''])
		#ジリアックス : <b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>
	elif ID == 'BT_155':
		myCondition.append(['taunt','', ''])
		#屑鉄山のコロッサス : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ7/7の「フェル漏れのコロッサス」を1体召喚する。
	elif ID == 'BT_715':
		myCondition.append(['taunt','', ''])
		#ボーンチューワーの喧嘩屋 : <b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。
	elif ID == 'BT_716':
		myCondition.append(['taunt','', ''])
		#ボーンチューワーの前衛 : <b>挑発</b>このミニオンがダメージを受ける度攻撃力+2を獲得する。
	elif ID == 'BT_720':
		myCondition.append(['taunt','', ''])
		#錆鉄騎の略奪者 : <b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。
	elif ID == 'BT_730':
		myCondition.append(['taunt','', ''])
		#大物気取りのオーク : <b>挑発</b>体力が最大の場合このミニオンは____攻撃力+2を得る。
	elif ID == 'CFM_652':
		myCondition.append(['taunt','', ''])
		#二流の強面 : [x]<b>挑発</b>相手の陣地に3体以上のミニオンがいる場合_____コストが（2）減る。
	elif ID == 'CFM_653':
		myCondition.append(['taunt','', ''])
		#日雇い護衛 : <b>挑発</b>
	elif ID == 'CFM_688':
		myCondition.append(['taunt','', ''])
		#トゲ付きのホグライダー : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。
	elif ID == 'CFM_790':
		myCondition.append(['taunt','', ''])
		#ドブネズミ : [x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。
	elif ID == 'CFM_806':
		myCondition.append(['taunt','', ''])
		#ラシオン : [x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。
	elif ID == 'CFM_854':
		myCondition.append(['taunt','', ''])
		#満開の古代樹 : <b>挑発</b>
	elif ID == 'CS1_042':
		myCondition.append(['taunt','', ''])
		#ゴールドシャイアの歩兵 : <b>挑発</b>
	elif ID == 'CS1_069':
		myCondition.append(['taunt','', ''])
		#フェン・クリーパー : <b>挑発</b>
	elif ID == 'CS2_121':
		myCondition.append(['taunt','', ''])
		#フロストウルフの兵卒 : <b>挑発</b>
	elif ID == 'CS2_125':
		myCondition.append(['taunt','', ''])
		#鉄毛のグリズリー : <b>挑発</b>
	elif ID == 'CS2_127':
		myCondition.append(['taunt','', ''])
		#シルバーバックの長 : <b>挑発</b>
	elif ID == 'CS2_162':
		myCondition.append(['taunt','', ''])
		#闘技場の覇者 : <b>挑発</b>
	elif ID == 'CS2_179':
		myCondition.append(['taunt','', ''])
		#センジン・シールドマスタ : <b>挑発</b>
	elif ID == 'CS2_187':
		myCondition.append(['taunt','', ''])
		#ブーティ・ベイのボディガード : <b>挑発</b>
	elif ID == 'DAL_058':
		myCondition.append(['taunt','', ''])
		#ヤジロボ : <b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。
	elif ID == 'DAL_088':
		myCondition.append(['taunt','', ''])
		#金庫番 : <b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ0/5の「金庫」を1体召喚する。
	elif ID == 'DAL_096':
		myCondition.append(['taunt','', ''])
		#ヴァイオレット監獄の看守 : <b>挑発</b><b>呪文ダメージ+1</b>
	elif ID == 'DAL_551':
		myCondition.append(['taunt','', ''])
		#誇り高き守護者 : [x]<b>挑発</b>味方に他のミニオンがいない場合__攻撃力+2を得る。
	elif ID == 'DAL_560':
		myCondition.append(['taunt','', ''])
		#酒場のヒロイック女将 : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_
	elif ID == 'DAL_775':
		myCondition.append(['taunt','', ''])
		#トンネル爆破係 : [x]<b>挑発</b>、<b>断末魔:</b>全てのミニオンに____3ダメージを与える。
	elif ID == 'DRG_064':
		myCondition.append(['taunt','', ''])
		#ズルドラクの儀式官 : [x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__
	elif ID == 'DRG_065':
		myCondition.append(['taunt','', ''])
		#ヒポグリフ : <b>急襲</b>、<b>挑発</b>
	elif ID == 'DRG_242':
		myCondition.append(['taunt','', ''])
		#ガラクロンドの盾 : <b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
	elif ID == 'EX1_002':
		myCondition.append(['taunt','', ''])
		#黒騎士 : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。
	elif ID == 'EX1_032':
		myCondition.append(['taunt','', ''])
		#サンウォーカー : [x]<b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'EX1_058':
		myCondition.append(['taunt','', ''])
		#サンフューリーの護衛 : [x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。
	elif ID == 'EX1_093':
		myCondition.append(['taunt','', ''])
		#アルガスの守護者 : <b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。
	elif ID == 'EX1_097':
		myCondition.append(['taunt','', ''])
		#涜れしもの : [x]<b>挑発</b>、<b>断末魔:</b> 全てのキャラクターに　2ダメージを与える。
	elif ID == 'EX1_390':
		myCondition.append(['taunt','', ''])
		#トーレン・ウォリアー : [x]<b>挑発</b>ダメージを受けている間は___攻撃力+3を得る。
	elif ID == 'EX1_396':
		myCondition.append(['taunt','', ''])
		#魔古山の番兵 : <b>挑発</b>
	elif ID == 'EX1_405':
		myCondition.append(['taunt','', ''])
		#盾持ち : <b>挑発</b>
	elif ID == 'FP1_012':
		myCondition.append(['taunt','', ''])
		#ヘドロゲッパー : [x]<b>挑発・断末魔:</b> <b>挑発</b>を持つ1/2のスライムを1体召喚する。
	elif ID == 'FP1_024':
		myCondition.append(['taunt','', ''])
		#不安定なグール : [x]<b>挑発</b>、<b>断末魔:</b> 全てのミニオンに____1ダメージを与える。
	elif ID == 'GIL_120':
		myCondition.append(['taunt','', ''])
		#怒れるエティン : <b>挑発</b>
	elif ID == 'GIL_207':
		myCondition.append(['taunt','', ''])
		#幽霊民兵 : <b>木霊</b>、<b>挑発</b>
	elif ID == 'GIL_526':
		myCondition.append(['taunt','', ''])
		#ワームガード : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。
	elif ID == 'GIL_527':
		myCondition.append(['taunt','', ''])
		#フェルソウルの異端審問官 : <b>生命奪取</b>、<b>挑発</b>
	elif ID == 'GIL_623':
		myCondition.append(['taunt','', ''])
		#ウィッチウッドのグリズリー : [x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。
	elif ID == 'GIL_667':
		myCondition.append(['taunt','', ''])
		#朽ちかけたアップルバウム : [x]<b>挑発</b>、<b>断末魔:</b>自分のヒーローの体力を#4回復する。
	elif ID == 'GIL_809':
		myCondition.append(['taunt','', ''])
		#眠るスチームロボ : <b>挑発</b>
	elif ID == 'GVG_085':
		myCondition.append(['taunt','', ''])
		#マジウザ・オ・トロン : <b>挑発</b><b>聖なる盾</b>
	elif ID == 'GVG_093':
		myCondition.append(['taunt','', ''])
		#ターゲット・ダミー : <b>挑発</b>
	elif ID == 'GVG_097':
		myCondition.append(['taunt','', ''])
		#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
	elif ID == 'GVG_098':
		myCondition.append(['taunt','', ''])
		#ノームレガン歩兵 : [x]<b>突撃</b>、<b>挑発</b>
	elif ID == 'GVG_107':
		myCondition.append(['taunt','', ''])
		#エンハンス・オ・メカーノ : <b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>
	elif ID == 'ICC_314':
		myCondition.append(['taunt','', ''])
		#リッチキング : [x]<b>挑発</b>自分のターンの終了時ランダムな<b>デスナイト</b>カード1枚を自分の手札に追加する。
	elif ID == 'ICC_466':
		myCondition.append(['taunt','', ''])
		#サロナイト鉱山の奴隷 : [x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。
	elif ID == 'ICC_705':
		myCondition.append(['taunt','', ''])
		#ボーンメア : [x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。
	elif ID == 'ICC_853':
		myCondition.append(['taunt','', ''])
		#ヴァラナール公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。
	elif ID == 'ICC_912':
		myCondition.append(['taunt','', ''])
		#躯の駆り手 : [x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。
	elif ID == 'KAR_011':
		myCondition.append(['taunt','', ''])
		#気取り屋の俳優 : <b>挑発</b>
	elif ID == 'KAR_037':
		myCondition.append(['taunt','', ''])
		#番鳥 : <b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。
	elif ID == 'KAR_061':
		myCondition.append(['taunt','', ''])
		#キュレーター : [x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。
	elif ID == 'KAR_710':
		myCondition.append(['taunt','', ''])
		#魔力細工師 : <b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。
	elif ID == 'LOE_073':
		myCondition.append(['taunt','', ''])
		#デビルサウルスの化石 : <b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。
	elif ID == 'LOOT_117':
		myCondition.append(['taunt','', ''])
		#蝋のエレメンタル : <b>挑発</b><b>聖なる盾</b>
	elif ID == 'LOOT_124':
		myCondition.append(['taunt','', ''])
		#孤高の勇者 : [x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。
	elif ID == 'LOOT_131':
		myCondition.append(['taunt','', ''])
		#グリーン・ジェリー : [x]自分のターンの終了時<b>挑発</b>を持つ1/2のウーズを1体召喚する。
	elif ID == 'LOOT_137':
		myCondition.append(['taunt','', ''])
		#眠れるドラゴン : <b>挑発</b>
	elif ID == 'LOOT_315':
		myCondition.append(['taunt','', ''])
		#トログのキノコ食い : [x]<b>挑発</b>、<b>猛毒</b>
	elif ID == 'LOOT_383':
		myCondition.append(['taunt','', ''])
		#飢えているエティン : <b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。
	elif ID == 'NEW1_022':
		myCondition.append(['taunt','', ''])
		#悪辣なる海賊 : [x]<b>挑発</b>自分の武器の攻撃力1につき_____コストが（1）減る。
	elif ID == 'NEW1_040':
		myCondition.append(['taunt','', ''])
		#ホガー : [x]自分のターンの終了時<b>挑発</b>を持つ2/2のノールを1体召喚する。
	elif ID == 'OG_131':
		myCondition.append(['taunt','', ''])
		#双皇帝ヴェク＝ロア : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。
	elif ID == 'OG_145':
		myCondition.append(['taunt','', ''])
		#マジヤバ・オ・トロン : <b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'OG_153':
		myCondition.append(['taunt','', ''])
		#変・クリーパー : <b>挑発</b>
	elif ID == 'OG_156':
		myCondition.append(['taunt','', ''])
		#マーロックの鯛ド変態 : [x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。
	elif ID == 'OG_174':
		myCondition.append(['taunt','', ''])
		#さまよう無貌のもの : [x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。
	elif ID == 'OG_249':
		myCondition.append(['taunt','', ''])
		#蝕まれしトーレン : [x]<b>挑発</b>、<b>断末魔:</b> 2/2のスライムを1体召喚する。
	elif ID == 'OG_284':
		myCondition.append(['taunt','', ''])
		#黄昏の鎚の地霊術師 : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>
	elif ID == 'OG_318':
		myCondition.append(['taunt','', ''])
		#エルウィンの変災ホガー : [x]このミニオンがダメージを受ける度<b>挑発</b>を持つ2/2の　ノールを1体召喚する。
	elif ID == 'OG_327':
		myCondition.append(['taunt','', ''])
		#のたうつ触手 : <b>挑発</b>
	elif ID == 'OG_337':
		myCondition.append(['taunt','', ''])
		#単眼の怪異 : [x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。
	elif ID == 'SCH_232':
		myCondition.append(['taunt','', ''])
		#クリムゾンの竜学生 : [x]<b>魔法活性:</b>攻撃力+1と<b>挑発</b>を獲得する。
	elif ID == 'SCH_709':
		myCondition.append(['taunt','', ''])
		#イキってる四年生 : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ5/7の幽霊1体を自分の___手札に追加する。
	elif ID == 'SCH_710':
		myCondition.append(['taunt','', ''])
		#往餓術師 : [x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。
	elif ID == 'TRL_363':
		myCondition.append(['taunt','', ''])
		#サロナイト鉱山の奴隷監督 : [x]<b>断末魔:</b><b>挑発</b>を持つ0/3の「FA宣言選手」を1体____相手の陣地に召喚する。
	elif ID == 'TRL_513':
		myCondition.append(['taunt','', ''])
		#モッシュオグの審判 : <b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'TRL_514':
		myCondition.append(['taunt','', ''])
		#大虎ノーム : [x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。
	elif ID == 'TRL_515':
		myCondition.append(['taunt','', ''])
		#会場警備係 : [x]<b>挑発</b>敵のミニオン1体につきコストが（1）減る。
	elif ID == 'TRL_524':
		myCondition.append(['taunt','heHasTaunt(game)', 'silence'])
		#シールドブレイカー : <b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。
	elif ID == 'TRL_550':
		myCondition.append(['taunt','', ''])
		#アマニの戦熊 : <b>急襲</b>、<b>挑発</b>
	elif ID == 'ULD_178':
		myCondition.append(['taunt','', ''])
		#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
	elif ID == 'ULD_179':
		myCondition.append(['taunt','', ''])
		#ファランクス指揮官 : [x]味方の<b>挑発</b>を持つミニオン全ては攻撃力+2を得る。
	elif ID == 'ULD_189':
		myCondition.append(['taunt','', ''])
		#無貌の潜むもの : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンの体力を2倍にする。
	elif ID == 'ULD_193':
		myCondition.append(['taunt','', ''])
		#動くモニュメント : <b>挑発</b>
	elif ID == 'ULD_198':
		myCondition.append(['taunt','', ''])
		#うつろう蜃気楼 : [x]<b>挑発</b>自分のターンの開始時このミニオンを____自分のデッキに混ぜる。
	elif ID == 'ULD_208':
		myCondition.append(['taunt','', ''])
		#カルトゥートの守護者 : [x]<b>挑発</b>、<b>蘇り</b><b>断末魔:</b>自分のヒーローの_____体力を#3回復する。
	elif ID == 'ULD_215':
		myCondition.append(['taunt','', ''])
		#包帯ゴーレム : [x]<b>蘇り</b>自分のターンの終了時<b>挑発</b>を持つ1/1の「スカラベ」を1体召喚する。
	elif ID == 'ULD_250':
		myCondition.append(['taunt','', ''])
		#虫食いゴブリン : [x]<b>挑発</b>、<b>断末魔:</b><b>挑発</b>を持つ1/1の「スカラベ」2体を____自分の手札に追加する。
	elif ID == 'ULD_271':
		myCondition.append(['taunt','', ''])
		#傷を負ったトルヴィア : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンに____3ダメージを与える。
	elif ID == 'ULD_275':
		myCondition.append(['taunt','', ''])
		#ボーン・レイス : <b>挑発</b>、<b>蘇り</b>
	elif ID == 'UNG_070':
		myCondition.append(['taunt','', ''])
		#トルヴィアのストーンシェイパー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。
	elif ID == 'UNG_071':
		myCondition.append(['taunt','', ''])
		#巨大マストドン : <b>挑発</b>
	elif ID == 'UNG_072':
		myCondition.append(['taunt','', ''])
		#ストーンヒルの守護者 : [x]<b>挑発</b>、<b>雄叫び:</b><b>挑発</b>を持つミニオン____1体を<b>発見</b>する。
	elif ID == 'UNG_801':
		myCondition.append(['taunt','', ''])
		#巣作りロック鳥 : [x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。
	elif ID == 'UNG_808':
		myCondition.append(['taunt','', ''])
		#不屈のカタツムリ : [x]<b>挑発</b>、<b>猛毒</b>
	elif ID == 'UNG_810':
		myCondition.append(['taunt','', ''])
		#ステゴドン : <b>挑発</b>
	elif ID == 'UNG_848':
		myCondition.append(['taunt','', ''])
		#始祖ドレイク : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。
	elif ID == 'UNG_907':
		myCondition.append(['taunt','', ''])
		#オズラック : [x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。
	elif ID == 'UNG_928':
		myCondition.append(['taunt','', ''])
		#タール・クリーパー : [x]<b>挑発</b>相手のターン中は___攻撃力+2を得る。
	elif ID == 'YOD_038':
		myCondition.append(['taunt','', ''])
		#空賊大将クラッグ : [x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。
	return myCondition
