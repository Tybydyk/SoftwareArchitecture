package homework_3.ISP;

public class Circle implements Shape {
    private int radius;

    public int getRadius() {
        return radius;
    }

    @Override
    public double perimeter() {
        return radius * 2 * 3.14;
    }
}
