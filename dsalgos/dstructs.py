"""A module to to work with Data Structures

(with documentation for everything in detail, for beginners)
"""


# Import `annotations` from `__future__` for delayed annotations
from __future__ import annotations


__all__ = ('Data', 'Node', 'Array', 'LinkedList')


# Import `array` from `array` as `_Array` for C type arrays
from array import array as _Array

# Import `typing` for type annotations
import typing


# Type/Class of `None` (NoneType)
NoneType = type(None)


class Data:
    """Data class to store any data, in any no. of *args* \
(arguments) and *kwargs* (keyword arguments)
"""
    def __init__(self, *args, **kwargs) -> NoneType:
        self.args = args
        self.kwargs = kwargs

        return None

    def __repr__(self) -> str:
        return f'Data{self.data}'

    def __eq__(self, data) -> bool:
        if isinstance(data, Data):
            return self.data == data.data
        
        return False

    def __bool__(self) -> bool:
        return self != Data()
    
    def __hash__(self) -> int:
        return hash(self.data)
    
    def __contains__(self, value) -> bool:
        return value in self.data.values()
    
    def __iter__(self):
        return iter(self.data.values())

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value) -> NoneType:
        try:
            self.args[key] = value

        except TypeError:
            self.kwargs[key] = value

        return None

    def __add__(self, data) -> Data:
        if isinstance(data, Data):
            return Data(
                *self.args, *data.args,
                **self.kwargs, **data.kwargs
            )
        
        raise TypeError(f"'{data}' must be of type 'Data'")
    
    def __iadd__(self, data) -> NoneType:
        if isinstance(data, Data):
            self.args = self.args + data.args
            self.kwargs.update(data.kwargs)
        
        raise TypeError(f"'{data}' must be of type 'Data'")
    
    @property
    def data(self) -> dict:
        return {
            **dict(enumerate(self.args)),
            **self.kwargs
        }


class Node:
    """Instantiates a basic node object

Parameters
    data=0 (object) - An object of any datatype
    parent=None (Node) - A Node object as the parent
    children=[] (list|tuple|set) - A list of children Node objects
    previous=None (Node) - A Node object before the current Node
    object in a collection (e.g., LinkedList, Stack,
        Queue, etc., objects)
    next_=None (Node) - A Node object after the current Node object
    in a collection (e.g., LinkedList, Stack, Queue, etc., objects)
    action=None (*) - Any kind of a custom action

Example
    node = Node()

Explanation
    A node is a basic unit of a data structure,
    such as a linked list or tree data structure.
    Nodes contain data and also may link to other nodes.
    Links between nodes are often implemented by pointers.

    Nodes are often arranged into tree structures. A node represents
    the information contained in a single data structure. These nodes
    may contain a value or condition, or possibly serve as another
    independent data structure. Nodes are represented by a single
    parent node. The highest point on a tree structure is called a
    root node, which does not have a parent node, but serves as the
    parent or 'grandparent' of all of the nodes below it in the tree.
    The height of a node is determined by the total number of edges
    on the path from that node to the furthest leaf node, and the
    height of the tree is equal to the height of the root node.
    Node depth is determined by the distance between that particular
    node and the root node. The root node is said to have a depth of
    zero. Data can be discovered along these network paths. An IP
    address uses this kind of system of nodes to define its location
    in a network.
"""

    def __init__(
        self, data: Data = Data(),
        parent: typing.Union[Node, NoneType] = None,
        children: typing.Union[
            typing.List[Node],
            typing.Tuple[Node],
            typing.Set[Node]
        ] = [],
        previous: typing.Union[Node, NoneType] = None,
        next_: typing.Union[Node, NoneType] = None,
        action = None
    ) -> NoneType:
        for attr in (parent, previous, next_):
            if not isinstance(attr, (Node, NoneType)):
                raise TypeError("parent, previous, \
and next_ must be 'None' or of type 'Node'")

        if not isinstance(children, (list, tuple, set)):
            raise TypeError("children must be of \
type list|tuple|set containing 'Node' objects")
        
        self.data = data
        self._parent = parent

        if isinstance(parent, Node):
            self.parent.children.append(self)

        self.children = list(children)

        for child in children:
            if isinstance(child, Node):
                child.parent = self

            else:
                raise TypeError(f"{child} must be of type 'Node'")
            
        self._previous = previous

        if isinstance(previous, Node):
            self.previous.next_ = self
            
        self._next = next_

        if isinstance(next_, Node):
            self.next_.previous = self
            
        self.action = action

        return None

    def __repr__(self) -> str:
        return (
            f'Node({repr(self.data)}, {repr(self.parent)}, '
            f'{repr(self.children)}, {repr(self.previous)},'
            f' {repr(self.next_)}, {repr(self.action)})'
        )

    def __len__(self) -> int:
        return len(self.children)

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, Node):
            return (
                self.data == node.data
                and self.data == node.parent
                and self.children == node.children
                and self.previous == node.previous
                and self.next_ == node.next_
                and self.action == node.action
            )
        
        return False

    def __bool__(self) -> bool:
        return self == Node()
    
    def __hash__(self) -> int:
        return hash((self.data, self.action))
    
    def __iter__(self):
        return iter(self.children)
        
    def __contains__(self, child: Node) -> bool:
        return child in self.children

    @property
    def parent(self) -> typing.Union[Node, NoneType]:
        return self._parent

    @parent.setter
    def parent(self, parent: typing.Union[Node, NoneType]) -> NoneType:
        if not isinstance(parent, (Node, NoneType)):
            raise TypeError("parent must be 'None' or of type 'Node'")
        
        self._parent = parent

        if isinstance(parent, Node):
            if self not in parent.children:
                self.previous = (
                    parent.children[-1]
                    if len(parent.children) > 0
                    else None
                )
                
                parent.children.append(self)

        return None

    @property
    def previous(self) -> typing.Union[Node, NoneType]:
        return self._previous

    @previous.setter
    def previous(self, previous: typing.Union[Node, NoneType]) -> NoneType:
        if not isinstance(previous, (Node, NoneType)):
            raise TypeError("previous must be 'None' or of type 'Node'")

        self._previous = previous

        if isinstance(previous, Node):
            if self != previous.next_:
                previous.next_ = self
                self.parent = previous.parent

        return None

    @property
    def next_(self) -> typing.Union[Node, NoneType]:
        return self._next

    @next_.setter
    def next_(self, next_: typing.Union[Node, NoneType]) -> NoneType:
        if not isinstance(next_, (Node, NoneType)):
            raise TypeError("next_ must be 'None' or of type 'Node'")
        
        self._next = next_

        if isinstance(next_, Node):
            if self != next_.previous:
                next_.previous = self
                self.parent = next_.parent

        return None

    @property
    def degree(self) -> int:
        """Returns the degree, i.e., the no. of children of node object

Returned value also accessible directly using:
len(node.children)
"""
        
        return len(self)

    @property
    def depth(self) -> int:
        """Returns the depth of node object

'depth' of a node object is the length of the path
between the root/main parent node object and the
current node object, or the no. of node objects
between the root and the current node objects
"""
        
        depth = 0
        currentnode = self

        while currentnode.parent is not None:
            depth = depth + 1
            currentnode = currentnode.parent

        return depth

    @property
    def isinternal(self):
        """Returns True if the node object is internal, \
else returns False

A node object is 'internal' when it has at least one child node,
the opposite of an 'external' node

Returned value also accessible directly using:
len(node) >= 1
"""
        
        return len(self) >= 1

    @property
    def isexternal(self) -> bool:
        """Returns True if the node object is external, \
else returns False

A node object is 'external' when it has no child nodes,
the opposite of an 'internal' node

Returned value also accessible directly using:
len(node) == 0
"""
        
        return len(self) == 0

    @property
    def isroot(self) -> bool:
        """Returns True if the node object is the root node, \
else returns False

A 'root' node is the main parent node
"""
        
        return self.parent is None

    @property
    def siblings(self) -> tuple:
        """Returns a list of all siblings of a node object \
(includes the current node object if *include_self* is True)

A 'sibling' is a node object with the same
parent node as the current Node object
"""
        
        if self.isroot:
            return ()
        
        siblings = self.parent.children
        siblings.remove(self)

        return tuple(siblings)


class Array(_Array):
    """Array(typecode [, initializer]) -> Array

Return a new Array whose items are restricted by typecode, and
initialized from the optional initializer value, which must be a list,
string or iterable over elements of the appropriate type.

Arrays represent basic values and behave very much like lists, except
the type of objects stored in them is constrained. The type is specified
at object creation time by using a type code, which is a single character.
The following type codes are defined:
    Type code   C Type             Minimum size in bytes
    'b'         signed integer     1
    'B'         unsigned integer   1
    'u'         Unicode character  2 (see note)
    'h'         signed integer     2
    'H'         unsigned integer   2
    'i'         signed integer     2
    'I'         unsigned integer   2
    'l'         signed integer     4
    'L'         unsigned integer   4
    'q'         signed integer     8 (see note)
    'Q'         unsigned integer   8 (see note)
    'f'         floating point     4
    'd'         floating point     8

NOTE: The 'u' typecode corresponds to Python's unicode character. On
narrow builds this is 2-bytes on wide builds this is 4-bytes.

NOTE: The 'q' and 'Q' type codes are only available if the platform
C compiler used to build Python supports 'long long', or, on Windows,
'__int64'.

Methods:

append() -- append a new item to the end of the array
buffer_info() -- return information giving the current memory info
byteswap() -- byteswap all the items of the array
count() -- return number of occurrences of an object
extend() -- extend array by appending multiple elements from an iterable
fromfile() -- read items from a file object
fromlist() -- append items from the list
frombytes() -- append items from the string
index() -- return index of first occurrence of an object
insert() -- insert a new item into the array at a provided position
pop() -- remove and return item (default last)
remove() -- remove first occurrence of an object
reverse() -- reverse the order of the items in the array
tofile() -- write all items to a file object
tolist() -- return the array converted to an ordinary list
tobytes() -- return the array converted to a string

Attributes:

typecode -- the typecode character used to create the array
itemsize -- the length in bytes of one array item
"""

    pass


class SinglyLinkedList:
    """Instantiates a Singly Linked List object

Parameters
    head=None (Node) - A head node object (at index = 0)
    elements=[] (list|tuple|set) - A default list of node objects

Example
    sllist = SinglyLinkedList()

Explanation
    A linked list is a linear collection of data elements, whose
    order is not given by their physical placement in memory,
    instead, each element points to the next. It is a data
    structure consisting of a collection of nodes which together
    represent a sequence. In its most basic form, each node contains:
    data, and a reference (in other words, a link) to the next node
    in the sequence. This structure allows for efficient insertion or
    removal of elements from any position in the sequence during
    iteration. More complex variants add additional links, allowing
    more efficient insertion or removal of nodes at arbitrary
    positions. A drawback of linked lists is that access time is
    linear (and difficult to pipeline). Faster access, such as random
    access, is not feasible. Arrays have better cache locality
    compared to linked lists.

    Linked lists are among the simplest and most common data structures
    They can be used to implement several other common abstract data
    types, including lists, stacks, queues, associative arrays, and
    S-expressions, though it is not uncommon to implement those data
    structures directly without using a linked list as the basis.

    The principal benefit of a linked list over a conventional array
    is that the list elements can be easily inserted or removed
    without reallocation or reorganization of the entire structure
    because the data items need not be stored contiguously in memory
    or on disk, while restructuring an array at run-time is a much
    more expensive operation. Linked lists allow insertion and
    removal of nodes at any point in the list, and allow doing so
    with a constant number of operations by keeping the link previous
    to the link being added or removed in memory during list traversal.

    On the other hand, since simple linked lists by themselves do not
    allow random access to the data or any form of efficient indexing,
    many basic operations—such as obtaining the last node of the list,
    finding a node that contains a given datum, or locating the place
    where a new node should be inserted—may require iterating through
    most or all of the list elements. The advantages and disadvantages
    of using linked lists are given below. Linked list are dynamic, so
    the length of list can increase or decrease as necessary. Each
    node does not necessarily follow the previous one physically
    in the memory.
"""

    def __init__(
        self,
        head: typing.Union[Node, NoneType] = None,
        elements: typing.Union[
            typing.List[Node],
            typing.Tuple[Node],
            typing.Set[Node]
        ] = []
    ) -> NoneType:
        if not isinstance(head, (Node, NoneType)):
            raise TypeError("'head' must be 'None' or of type 'Node'")
        
        if not isinstance(elements, (list, tuple, set)):
            raise TypeError("'elements' \
must be a list|tuple|set of 'Node' objects")

        self._head = head
        self._elements = []

        for i, element in enumerate(elements := list(elements)):
            if not isinstance(element, Node):
                raise TypeError(f"'{element}' must be of type 'Node'")
            
            if i < len(elements) - 1:
                element.next_ = elements[i+1]
            
            self._elements.append(element)
        
        if isinstance(head, Node) and len(self._elements) > 0:
            self._head.next_ = self._elements[0]
        
        return None
    
    def __repr__(self) -> str:
        return f'SinglyLL({self.head}, {self.elements})'
    
    def __eq__(self, sllist) -> bool:
        if isinstance(sllist, SinglyLinkedList):
            return (
                self.head == sllist.head and
                self.elements == sllist.elements
            )
        
        return False
    
    def __bool__(self) -> bool:
        return bool(self.elements)
    
    def __len__(self) -> int:
        return len(self.elements)
    
    def __iter__(self):
        return iter(self.elements)
    
    def __hash__(self) -> int:
        return hash((self.head, *self.elements))
    
    def __contains__(self, element) -> bool:
        return element in self.elements
    
    def __getitem__(self, index) -> Node:
        return self.elements[index]
    
    def __setitem__(self, index, element) -> NoneType:
        self.elements[index] = element
        
        if isinstance(index, int):
            if index > 0:
                self.elements[index-1].next_ = self.elements[index]
        
        return None
    
    def __add__(self, sllist) -> SinglyLinkedList:
        if not isinstance(sllist, SinglyLinkedList):
            raise TypeError(f"'{sllist}' must be of type 'SinglyLinkedList'")
        
        return SinglyLinkedList(self.head, self.elements+sllist.elements)
    
    def __iadd__(self, sllist) -> NoneType:
        if not isinstance(sllist, SinglyLinkedList):
            raise TypeError(f"'{sllist}' must be of type 'SinglyLinkedList'")
        
        self.elements.extend(sllist.elements)
        
        return None
    
    @property
    def head(self) -> Node:
        return self._head
    
    @head.setter
    def head(self, head) -> NoneType:
        self._head = head
        
        if isinstance(head, Node):
            self._head.next_ = self.elements[0]
        
        return None
    
    @property
    def elements(self) -> typing.Union[
        typing.List[Node], typing.Tuple[Node], typing.Set[Node]
    ]:
        return self._elements
    
    @elements.setter
    def elements(self, elements) -> NoneType:
        for element in self:
            element.next_ = None
        
        self._elements = []
        
        for i, element in enumerate(elements := list(elements)):
            if not isinstance(element, Node):
                raise TypeError(f"'{element}' must be of type 'Node'")
            
            if i < len(elements) - 1:
                element.next_ = elements[i+1]
            
            self._elements.append(element)
        
        return None
