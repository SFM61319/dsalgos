# Import `annotations` from `__future__` for delayed annotations
from __future__ import annotations


"""A module to to work with Data Structures

(with documentation for everything in detail, for beginners)
"""


__all__ = (
    'Data', 'Node'
)


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
        return self == Data()
    
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
type 'list'|'tuple'|'set' containing 'Node' objects")
        
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
