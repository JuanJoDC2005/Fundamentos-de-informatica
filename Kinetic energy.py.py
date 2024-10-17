def calculate_kinetic_energy(mass, velocity):

    kinetic_energy = 0.5 * mass * (velocity ** 2)
    return kinetic_energy


def main():
    try:
        mass = float(input("Enter the mass of the object in kilograms: "))
        velocity = float(
            input("Enter the velocity of the object in meters per second: "))

        kinetic_energy = calculate_kinetic_energy(mass, velocity)

        print(f"The kinetic energy is {kinetic_energy} joules.")

    except ValueError:
        print("Please enter valid numbers for mass and velocity.")


if __name__ == "__main__":
    main()
