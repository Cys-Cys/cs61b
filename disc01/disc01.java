public static List<Integer> evens(List<Integer> L) {
    List<Integer> list = new ArrayList<>();
    for (int num : L) {
        if (num % 2 == 0) {
            list.add(num);
        }
    }
    return list;
}

public static Map<String, Integer> countWords(List<String> words) {
    Map<String, Integer> map = new TreeMap<>();
    for (String word : words) {
        if (map.containsKey(word)) {
            map.put(word, map.get(word) + 1);
        } else {
            map.put(word, 1);
        }
    }
    return map;
}
