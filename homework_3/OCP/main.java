package homework_3.OCP;

public class main {
    public static void main(String[] args) {
        Vehicle vehicle = new Car(120);
        System.out.println(vehicle);
        vehicle = new Bus(120);
        System.out.println(vehicle);
        vehicle = new Vehicle(120, "vehicle");
        System.out.println(vehicle);
    }
}
