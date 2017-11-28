test for uploading pictures


# 149. Max Points on a Line
##Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

### url
![cats](https://i.pinimg.com/736x/a9/a3/46/a9a34606f68f5f86aa94833ad482e4c9--cute-pets-adorable-kittens.jpg)


### local
![cats2](/media/content/BlogPost/images/cats.jpeg)

```java
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
class Solution {
    public int maxPoints(Point[] points) {
        if (points == null || points.length == 0) return 0;
        Map<String, Integer> map = new HashMap<>();
        int res = 1;
        for (int i = 0; i < points.length; i++) {
            map.clear();
            int overlap = 1;
            for (int j = i + 1; j < points.length; j++) {
                int x = points[j].x - points[i].x;
                int y = points[j].y - points[i].y;
                if (x == 0 && y == 0) {
                    overlap++;
                    continue;
                }
                int gcd = generateGCD(x, y);
                if (gcd != 0) {
                    x /= gcd;
                    y /= gcd;
                }
                String key = x + "/" + y;
                map.put(key, map.getOrDefault(key, 0) + 1);
            }
            int local = 0;
            for (Integer num : map.values()) {
                local = Math.max(local, num);
            }
            res = Math.max(res, local + overlap);
        }
        return res;
    }
    
    private int generateGCD(int a, int b) {
        if (b == 0) {
            return a;            
        } else {
            return generateGCD(b, a % b);            
        }
    }
}
```