package homework_3.ISP;

public class Cube implements Shape3D{
    private int  side;

    public Cube(int side) {
        this.side = side;
    }

    public int getSide() {
        return side;
    }

    public double perimeter() {
        return side * side;
    }

    @Override
    public double value() {
        return side * side * side;
    }
}
