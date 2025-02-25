import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    """Return student enrollments and tuition fees as two lists."""
    enrollments = [uni[1] for uni in data]
    tuition = [uni[2] for uni in data]
    return enrollments, tuition

def mean(lst):
    """Calculate mean (average) of a list."""
    return sum(lst) / len(lst)

def median(lst):
    """Calculate median of a list."""
    return statistics.median(lst)

def main():
    """Main function to calculate and print university enrollment statistics."""
    enrollments, tuition = enrollment_stats(universities)
    total_students = sum(enrollments)
    total_tuition = sum(tuition)

    print("******************************")
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}\n")
    print(f"Student mean: {mean(enrollments):,.2f}")
    print(f"Student median: {median(enrollments):,}\n")
    print(f"Tuition mean: $ {mean(tuition):,.2f}")
    print(f"Tuition median: $ {median(tuition):,}")
    print("******************************")

if __name__ == "__main__":
    main()
