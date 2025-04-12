package personal;

public class Administrativo extends Empleado {
	 private String cargo;

	 public Administrativo(String nombre, int sueldoMes, String cargo) {
	     super(nombre, sueldoMes);
	     this.cargo = cargo;
	 }

	 @Override
	 public float sueldoTotal() {
	     return sueldoMes;
	 }
	}
