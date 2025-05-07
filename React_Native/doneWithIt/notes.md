This is based on a youtube video:
https://youtu.be/f8Z9JyB2EIE?si=rhNdm-dgzImOSNSM

{/_ <Text>Hello Abel</Text>
<TouchableHighlight onPress={() => console.log("image touched")}>
{/_ This is for local images _/}
{/_ <Image source={require("./assets/icon.png")} style={styles.logo} /> _/}
{/_ This is for network images _/}
{/_ <Image
source={{
            width: 200,
            height: 300,
            uri: "https://picsum.photos/200/300",
          }}
/> _/}
{/_ </TouchableHighlight> _/}
<StatusBar style="auto" /> _/}
