import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go


df_country = pd.read_csv("country.csv")
df_ability = pd.read_csv("All_players_ability_rev1.csv")

st.title("2022FIFAワールドカップ登録選手")
st.subheader("出場国・出場選手の特徴をサッカーゲームの能力値から把握しよう！")

st.subheader("■選手個人の能力比較")

st.write("比較選手①")
country_list = df_ability["国名"].unique()
option_country_1 = st.selectbox(
    "国名1",
    (country_list))
df_player_1 = df_ability[df_ability["国名"] == option_country_1]
player_list_1 = df_player_1["名前"].unique()
option_player_1 = st.selectbox(
    "選手名1",
    (player_list_1))
df_mean_player_1 = df_player_1[df_player_1["名前"] == option_player_1]

st.write("")

st.write("比較選手②")
option_country_2 = st.selectbox(
    "国名2",
    (country_list))
df_player_2 = df_ability[df_ability["国名"] == option_country_2]
player_list_2 = df_player_2["名前"].unique()
option_player_2 = st.selectbox(
    "選手名2",
    (player_list_2))
df_mean_player_2 = df_player_2[df_player_2["名前"] == option_player_2]


ability = ["クロス","決定力","ヘディング制度","ショートパス","ボレー","ドリブル","カーブ",\
            "FK精度","ロングパス","ボールコントロール","加速","トップスピード","俊敏性",\
            "リアクション","バランス","シュートパワー","ジャンプ","スタミナ","パワフル",\
            "ロングシュート","積極性","パスカット","ポジショニング","視野","ペナルティ",\
            "平静","防御意識","タックル","スライディング","GK ダイビング","GK ハンドリング",\
            "GK キック","GK ポジショニング","GK 反射神経"]


fig = go.Figure()
fig.add_trace(go.Bar(x=df_mean_player_1.iloc[0,3:37],
                y=ability,
                name=option_player_1,
                #marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=df_mean_player_2.iloc[0,3:37],
                y=ability,
                name=option_player_2,
                #marker_color='rgb(26, 118, 255)'
                ))

fig.update_xaxes(range=(0,100)) # X軸の最大最小値を指定

fig.update_layout(
    title='選手能力値の比較',
    xaxis=dict(
         title='能力値',
         titlefont_size=16,
         tickfont_size=14,
    ),
    yaxis=dict(
        title='能力名',
        titlefont_size=16,
        tickfont_size=14,
    ),
   legend=dict(orientation='h',
               xanchor='right',
               x=1,
               yanchor='bottom',
               y=1.05),
        width=750, 
        height=900,
        plot_bgcolor='white'
                  )
fig.update_traces(orientation="h"
            )


st.plotly_chart(fig)

st.subheader("■出場国の能力比較")

country_list = df_ability["国名"].unique()
option_country_3 = st.selectbox(
    "出場国1",
    (country_list))
df_country_3 = df_ability[df_ability["国名"] == option_country_3]
df_country_exceptGK_3 = df_country_3[df_country_3["ポジション"] != "GOALKEEPER"]
mean_country_3=[]
for i in range(3,32):
    mean_exceptGK_3 = df_country_exceptGK_3.iloc[:,i].mean()
    mean_country_3.append(mean_exceptGK_3)
df_country_GK_3 = df_country_3[df_country_3["ポジション"] == "GOALKEEPER"]
for i in range(32,37):
    mean_GK_3 = df_country_GK_3.iloc[:,i].mean()
    mean_country_3.append(mean_GK_3)

country_list = df_ability["国名"].unique()
option_country_4 = st.selectbox(
    "出場国2",
    (country_list))
df_country_4 = df_ability[df_ability["国名"] == option_country_4]
df_country_exceptGK_4 = df_country_4[df_country_4["ポジション"] != "GOALKEEPER"]
mean_country_4=[]
for i in range(3,32):
    mean_exceptGK_4 = df_country_exceptGK_4.iloc[:,i].mean()
    mean_country_4.append(mean_exceptGK_4)
df_country_GK_4 = df_country_4[df_country_4["ポジション"] == "GOALKEEPER"]
for i in range(32,37):
    mean_GK_4 = df_country_GK_4.iloc[:,i].mean()
    mean_country_4.append(mean_GK_4)

fig = go.Figure()
fig.add_trace(go.Bar(x=mean_country_3,
                y=ability,
                name=option_country_3,
                #marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=mean_country_4,
                y=ability,
                name=option_country_4,
                #marker_color='rgb(26, 118, 255)'
                ))

fig.update_xaxes(range=(0,100)) # X軸の最大最小値を指定

fig.update_layout(
    title='国別能力値の比較',
    xaxis=dict(
         title='能力値',
         titlefont_size=16,
         tickfont_size=14,
    ),
    yaxis=dict(
        title='能力名',
        titlefont_size=16,
        tickfont_size=14,
    ),
   legend=dict(orientation='h',
               xanchor='right',
               x=1,
               yanchor='bottom',
               y=1.05),
        width=750, 
        height=900,
        plot_bgcolor='white'
                  )
fig.update_traces(orientation="h"
            )


st.plotly_chart(fig)


st.write('本結果は https://www.fifa.com/fifaplus/ 及び https://sofifa.com/ を加工して作成')