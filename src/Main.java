public class Main {

    public static void main(String[] args) {
        String mJid = "anchor_1012518@bj2.1-1.io";
        String flag = "anchor_";
        if(mJid.startsWith(flag)){
            String sub_jid = mJid.replace(flag, "");
            System.out.println(sub_jid);
        }
        System.out.println("Hello World!");
    }
}
