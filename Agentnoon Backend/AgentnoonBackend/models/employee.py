from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
from typing import List, Dict, Tuple, ClassVar

@dataclass
class Employee:
    employee_id: int
    name: str
    job_title: str
    email: str
    manager_id: str
    status: str
    start_date: Optional[datetime]
    department: str
    location: str
    salary: float
    bonus: float
    end_date: Optional[datetime]
    photo: Optional[str]
    performance: Optional[str]
    project: Optional[str]
    entity: Optional[str]
    recruiting: Optional[str]
    skill: Optional[str]
    role: Optional[str]
    utilization: Optional[float]
    source: Optional[str]
    level: Optional[str]

    num_descendants: Optional[int] = field(init=False, default=None)

    management_cost: Optional[float] = field(init=False, default=None)
    ic_cost: Optional[float] = field(init=False, default=None)
    total_cost: Optional[float] = field(init=False, default=None)

    # todo I am not understanding the definition of the cost ratio
    # todo I need to ask about it and implement it

    manager: Optional["Employee"] = field(init=False, default=None)
    subordinates: Optional[List["Employee"]] = field(default_factory=list)

    ceo: ClassVar["Employee"] = None


    def __repr__(self):
        return f"<Employee {self.employee_id}: {self.name} - {self.job_title}>"


    def __str__(self):
        return (
            f"Employee[{self.employee_id}]: {self.name} - {self.job_title} \n"
            f"({self.department}, {self.location}) | \n"
            f"Email: {self.email} | Start: {self.start_date.date() if self.start_date else 'N/A'}"
        )
    

    def __hash__(self):
        return hash(self.employee_id)
    

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.employee_id == other.employee_id


    @classmethod
    def set_employee_tree(cls, employees: Dict[str, "Employee"]) -> "Employee":
        """Sets employee tree structure according to employee directory dictionary, sets the ceo, recursive fields
        If ceo is not none, a hard set is completed before setting the tree

        Arguments:
            employees -- a dictionary of employee_id to Employee

        Returns:
            CEO of employee tree, set for the class assumed to be single Employee that is not managed by any one
        """
        if cls.ceo is not None:
            cls.reset_tree_fields(hard=True) 

        unmanaged = set()
        for emp in employees.values():
            if emp.manager_id == '' or emp.manager_id is None:
                # employee has no managers
                unmanaged.add(emp)
            else:
                if emp in unmanaged:
                    # emp's manager is found, so let's remove it from the list of unmanged
                    unmanaged.remove(emp)
                
                manager = employees[emp.manager_id]
                emp.set_manager(manager)
                manager.add_subordinate(emp)
        
        assert(len(unmanaged) == 1)
        cls.ceo = unmanaged.pop()

        cls.ceo.get_recursive_fields(reset=True)
        return cls.ceo


    @classmethod
    def set_ceo(cls, ceo: "Employee") -> None:
        """Sets the ceo of the employee tree
        The ceo needs to be maintained by the client

        Arguments:
            ceo -- the root of the employee tree
        """
        cls.ceo = ceo
		

    @classmethod
    def get_bare_tree(cls) -> Dict[str, List[str]]:
        """
        Traverses the employee tree starting from the CEO and returns a dictionary where each key is an employee ID, 
        and the value is a list of IDs of their subordinates.
        """
        if cls.ceo is None:
            raise Exception("The CEO of the tree structure needs to be set before attempting to reset the tree")

        def traverse(employee: "Employee"):
            if len(employee.subordinates) == 0:
                return {employee.employee_id: []}

            my_subordinates = [traverse(subordinate) for subordinate in employee.subordinates]
            return {employee.employee_id: my_subordinates}

        return traverse(cls.ceo)

    
    @classmethod
    def reset_tree_fields(cls, hard=False) -> None:
        """Resets the recursive tree fields from the ceo

        Keyword Arguments:
            hard -- hard reset of the entire tree definition (default: {False})

        Raises:
            Exception: iff the ceo is None
        """
        if cls.ceo is None:
            raise Exception("The CEO of the tree structure needs to be set before attempting to reset the tree")
        q = []
        q.append(cls.ceo)
        while len(q) != 0:
            emp = q.pop()
            emp.management_cost = None
            emp.ic_cost = None
            emp.total_cost = None
            emp.num_descendants = None

            for sub in emp.subordinates:
                q.append(sub)

            if hard:
                emp.manager = None
                emp.subordinates = []
        
        if hard:
            cls.ceo = None


    def get_employee_dict(self):
        exclude_fields = ['manager', 'subordinates']

        data = {key: value for key, value in self.__dict__.items() if key not in exclude_fields}

        return data

    
    def set_manager(self, manager: "Employee") -> None:
        """Sets the manager to manager

        Arguments:
            manager -- manager to be set
        """
        self.manager = manager
    

    def add_subordinate(self, subordinate: "Employee") -> None:
        """Adds a subordinate to the list of subordinates

        Arguments:
            subordinate -- employee subordinate to be added
        """
        self.subordinates.append(subordinate)
        
    
    def is_individual(self) -> bool:
        """Returns true iff employee is an individual

        Returns:
            Returns true iff employee has no subordinates
        """
        return len(self.subordinates) == 0
    
        
    def get_recursive_fields(self, reset=False) -> Tuple[int, float, float, float, float]:
        """Gets all recursive fields, sets all the recursive fields eficiently iff any of them are None or reset is true

        Keyword Arguments:
            reset -- forces the recursive to be reset iff true (default: {False})

        Returns:
            tuple of:
            number of descendants (number of subordinates)
            management cost, the recursive sum of the salary of descendants who have subordinates reporting to them
            ic cost, the recursive sum of the salary of descendants who have **do not have** subordinates reporting to them
            total cost, the recursive sum of the salary of all descendants
        """
        if not reset and  \
            not any(x is None for x in (self.num_descendants, self.management_cost, self.ic_cost, self.total_cost)):
            return (self.num_descendants, self.management_cost, self.ic_cost, self.total_cost)

        # let's calculate it
        self.num_descendants = 0

        self.management_cost = 0.0
        self.ic_cost = 0.0
        self.total_cost = 0.0

        for subordinate in self.subordinates:
            s_num_descendants, s_management_cost, s_ic_cost, s_total_cost = subordinate.get_recursive_fields(reset=reset)
            s_salary = subordinate.salary
            assert(s_ic_cost + s_management_cost == s_total_cost)

            self.num_descendants += 1 + s_num_descendants

            if subordinate.is_individual():
                assert(s_ic_cost == 0)
                self.ic_cost += s_salary
            else:
                self.ic_cost += s_ic_cost
                self.management_cost += s_salary + s_management_cost
            self.total_cost += s_salary + s_ic_cost + s_management_cost

        return (self.num_descendants, self.management_cost, self.ic_cost, self.total_cost)
    

    def get_num_descendants(self, reset=False) -> int:
        """Gets the number of descendants, set it iff value is None or reset is true, recursively sets the number of descendants on children
        

        Keyword Arguments:
            reset -- forces the number of descendants to be reset iff true (default: {False})

        Returns:
            number of descendants (number of subordinates)
        """
        if not reset and self.num_descendants is not None:
            return self.num_descendants

        self.num_descendants = 0

        for subordinate in self.subordinates:
            self.num_descendants += 1 + subordinate.get_num_descendants(reset=reset)
        return self.num_descendants


    def get_management_cost(self, reset=False) -> float:
        """Gets the management cost, sets it iff value is None or reset is true, recursively sets the management cost of descendants
        

        Keyword Arguments:
            reset -- forces the management cost to be reset iff true (default: {False})

        Returns:
            the management cost, the recursive sum of the salary of descendants who have subordinates reporting to them
        """
        if not reset and self.management_cost is not None:
            return self.management_cost
        
        self.management_cost = 0.0

        for subordinate in self.subordinates:
            s_management_cost = subordinate.get_management_cost(reset=reset)
            if not subordinate.is_individual():
                self.management_cost += subordinate.salary + s_management_cost
        return self.management_cost


    def get_ic_cost(self, reset=False) -> float:
        """Gets the individual (ic) cost, sets it iff value is None or reset is true, recursively sets the ic cost of descendants
        

        Keyword Arguments:
            reset -- forces the ic cost to be reset iff true (default: {False})

        Returns:
            the ic cost, the recursive sum of the salary of descendants who have **do not have** subordinates reporting to them
        """
        if not reset and self.ic_cost is not None:
            return self.ic_cost

        self.ic_cost = 0.0

        for subordinate in self.subordinates:
            s_ic_cost = subordinate.get_ic_cost(reset=reset)
            if subordinate.is_individual():
                self.ic_cost += subordinate.salary
            else:
                self.ic_cost += s_ic_cost
        return self.ic_cost

    
    def get_total_cost(self, reset=False) -> float:
        """Gets the total cost, sets it iff value is None or reset is true, recursively sets the total cost of descendants
        sets the management cost and ic cost if they have not been set or if reset is true


        Keyword Arguments:
            reset -- forces the total cost **as well as the management cost and ic cost** to be reset iff true (default: {False})

        Returns:
            the total cost, the recursive sum of the salary of all descendants
        """
        if not reset:
            if self.total_cost is not None:
                return self.total_cost
            elif self.management_cost is not None and self.ic_cost is not None:
                return self.management_cost + self.ic_cost
            
            # try to do as little calculation as possible if one of the fields is at least set
            if self.management_cost is None and self.ic_cost is not None:
                return self.ic_cost + self.get_management_cost()
            elif self.ic_cost is None and self.management_cost is not None:
                return self.management_cost + self.get_ic_cost()

        self.management_cost = 0.0
        self.ic_cost = 0.0
        self.total_cost = 0.0

        for subordinate in self.subordinates:
            s_total_cost = subordinate.get_total_cost(reset=reset)
            s_management_cost, s_ic_cost = subordinate.management_cost, subordinate.ic_cost
            assert(s_ic_cost + s_management_cost == s_total_cost)

            if subordinate.is_individual():
                assert(s_ic_cost == 0)
                self.ic_cost += subordinate.salary
            else:
                self.ic_cost += s_ic_cost
                self.management_cost += subordinate.salary + s_management_cost
            self.total_cost += subordinate.salary + s_ic_cost + s_management_cost

        return self.total_cost