
def depth_first_search(node, visited):
  # Base case: if the node is null, return
  if node is None:
    return

  # Mark the node as visited to prevent cycles
  visited.add(node)

  # Do something with the node
  # This will depend on the specific problem you are trying to solve
  children = node.children

  # Recursively call the function on the children of the node
  for child in children:
    if child not in visited:

      # return the value if needed 
      depth_first_search(child, visited)
