import java.util.*;

public class Main {
    public static LinkedHashMap<String, AnchorWorkerMatcher> readyInMatch = new LinkedHashMap<>();

    public void test1(){
        String mJid = "anchor_1012518@bj2.1-1.io";
        String flag = "anchor_";
        if(mJid.startsWith(flag)){
            String sub_jid = mJid.replace(flag, "");
            System.out.println(sub_jid);
        }
        System.out.println("Hello World!");
    }

    public static void test2(){
        HashMap<String, Integer> readyInMatch =  new HashMap<>();
        for(int i=0; i<1000; i++){
            readyInMatch.put(String.valueOf(i), i);
        }
        int length = readyInMatch.keySet().size();
        Object[] avaliable = readyInMatch.keySet().toArray();
        List<Integer> generator = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            generator.add(i);
        }
        Collections.shuffle(generator);
        System.out.println(generator);
    }

    public static void test3(){
        String standard_jid = "anchor_1012518@bj2.1-1.io";
        int index = standard_jid.indexOf('@');
        String sub = standard_jid.substring(index);
        System.out.println(sub);
    }

    static HashSet<String> getOnlineAnchors() {
        HashSet<String> newOnline = new HashSet<>();
        newOnline.add("anchor_1006257@bj2.1-1.io");
        newOnline.add("anchor_1013919@bj2.1-1.io");
        newOnline.add("anchor_1008527@bj2.1-1.io");
        newOnline.add("anchor_1011744@bj2.1-1.io");
        newOnline.add("anchor_1007440@bj2.1-1.io");
        newOnline.add("anchor_1011729@bj2.1-1.io");
        newOnline.add("anchor_1012473@bj2.1-1.io");
        newOnline.add("anchor_1014939@bj2.1-1.io");
        newOnline.add("anchor_10062571@bj2.1-1.io");
        newOnline.add("anchor_10139191@bj2.1-1.io");
        newOnline.add("anchor_10085271@bj2.1-1.io");
        newOnline.add("anchor_10117441@bj2.1-1.io");
        newOnline.add("anchor_10074401@bj2.1-1.io");
        newOnline.add("anchor_10117291@bj2.1-1.io");
        newOnline.add("anchor_10149391@bj2.1-1.io");
        newOnline.add("anchor_10124731@bj2.1-1.io");
        return newOnline;
    }

    public static void initReadyInMatch(){
        HashSet<String> newOnline = new HashSet<>();
        newOnline.add("anchor_10062571@bj2.1-1.io");
        newOnline.add("anchor_10139191@bj2.1-1.io");
        newOnline.add("anchor_10085271@bj2.1-1.io");
        newOnline.add("anchor_10117441@bj2.1-1.io");
        newOnline.add("anchor_10074401@bj2.1-1.io");
        newOnline.add("anchor_10117291@bj2.1-1.io");
        newOnline.add("anchor_10149391@bj2.1-1.io");
        newOnline.add("anchor_10124731@bj2.1-1.io");
        for(String jid : newOnline){
            readyInMatch.put(jid, new AnchorWorkerMatcher(jid));
        }
    }

    /**
     * 将在线主播更新
     */
    public static void doUpdateSet() {
        initReadyInMatch();
        HashMap<String, AnchorWorkerMatcher> anchorInMatch = new HashMap<>();
        HashSet<String> newOnline = getOnlineAnchors();
        if (null != newOnline) {
            // 一直在线未被匹配
            HashSet<String> waitAppendMatch = new HashSet<>();
             waitAppendMatch.addAll(readyInMatch.keySet());
            System.out.printf("waitAppendMatch first : %d %n", waitAppendMatch.size());
            waitAppendMatch.retainAll(newOnline);
            // 差集：新在线的
            newOnline.removeAll(readyInMatch.keySet());
            for (String jid : newOnline) {
                anchorInMatch.put(jid, new AnchorWorkerMatcher(jid));
            }

            System.out.printf("waitAppendMatch two : %d %n", waitAppendMatch.size());
            for (String jid : waitAppendMatch) {
                anchorInMatch.put(jid, readyInMatch.get(jid));
            }

            // 清空
            readyInMatch.clear();
            System.out.printf("waitAppendMatch third : %d %n", waitAppendMatch.size());
            // 先添加旧的
            for(String jid : waitAppendMatch){
                readyInMatch.put(jid, anchorInMatch.get(jid));
                System.out.printf("waitAppendMatch jid: %s %n", jid);
            }

            // 新在线的加随机，入队列
            int length = newOnline.size();
            Object[] avaliable = newOnline.toArray();

            // 随机索引：随机取值
            List<Integer> generator = new ArrayList<>();
            for (int i = 0; i < length; i++) {
                generator.add(i);
            }
            Collections.shuffle(generator);
            for (int index : generator) {
//                jid = "anchor_1012518@bj2.1-1.io"; // 固定jid方便客户端测试
                // 随机获取jid
                String randomJid = (String) avaliable[index];
                AnchorWorkerMatcher anchor = anchorInMatch.get(randomJid);

                if (anchor != null) {
                    readyInMatch.put(randomJid, anchor);
                    System.out.printf("new jid: %s %n", randomJid);
                }
            }
        }
    }

    public static void test4(){
        doUpdateSet();
        for(String jid : readyInMatch.keySet()){
            AnchorWorkerMatcher anchor = readyInMatch.get(jid);
            System.out.printf("jid: %s, AnchorWorkerMatcher(id: %s, createTimestamp:%d) %n", jid, anchor.id, anchor.createTimestamp);
        }
    }

    public static void test5(){
        String isProduct = "true";
//        String isProduct = "false";
        boolean check = Boolean.parseBoolean(isProduct);
        boolean check1 = Boolean.getBoolean(isProduct);
        System.out.printf("check: %b, check1:%b", check, check1);
    }

    public static void main(String[] args) {
        test5();
    }
}

class AnchorWorkerMatcher{
    public long createTimestamp = System.currentTimeMillis();
    public String id;
    public AnchorWorkerMatcher(String jid){
        this.id = jid;
    }
}
