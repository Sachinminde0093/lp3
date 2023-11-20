// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Define a structure to represent student data
    struct Student {
        uint256 id;
        string name;
        uint256 age;
    }

    // Array to store student data
    Student[] public students;

    // Non-payable fallback function
    fallback() external {
        revert("This contract does not accept Ether");
    }

    // Function to add a new student
    function addStudent(string memory _name, uint256 _age) public {
        uint256 studentId = students.length + 1;
        students.push(Student(studentId, _name, _age));
    }

    // Function to get the details of a specific student
    function getStudent(uint256 _studentId) public view returns (uint256, string memory, uint256) {
        require(_studentId > 0 && _studentId <= students.length, "Invalid student ID");
        Student memory student = students[_studentId - 1];
        return (student.id, student.name, student.age);
    }

    // Function to get the total number of students
    function getNumberOfStudents() public view returns (uint256) {
        return students.length;
    }
}