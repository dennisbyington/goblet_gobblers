# ---------------------------------------------------------------------------
# Name of program(s): 

aStar_main.py

	# Helper files:
		
	aStar_args.py
	aStar_getH.py
	aStar_getPath.py
	aStar_Node.py
	aStar_printResults.py
	aStar_search.py

# ---------------------------------------------------------------------------
# Description 

A-Star Pathfinding (A*) implemented in python
  
  1) Parses command line arguments (if any)
    - default values are 4-way moves with the Manhattan heuristic
  
  2) Creates a default grid with barriers

  3) Performs A* on default grid with assigned allowed moves and heuristic
  
  3) Displays result
    

# ---------------------------------------------------------------------------
# Dependencies

- Python3 (shebang sets this)
- Imports: argparse, numpy, and heapq libraries


# ---------------------------------------------------------------------------
# Installing

Download all files to local folder


# ---------------------------------------------------------------------------
# Executing program

Open an instance of your shell and navigate to folder where the files were saved:
  - Invoke the A* program by calling: ./aStar_main.py
  - The default [m] value is 4
  - The default [H] value is 1 (Manhattan)
    - You may override these by providing alternate values to the -m/--moves or -H/--Heuristic options 

Note: 
If you encounter a "Permission denied" error when attempting to execute the files, the execution permission was likely removed when transferring the file to/from canvas.  If this error is encountered, please add the execution permissions back to the file by invoking the following in your shell from within the same folder as the file is saved:
	chmod +x aStar_main.py
	

Once the permission have been re-added, try to run the file again using the steps above.  


# ---------------------------------------------------------------------------
# Help
  
Help can be obtained by including the [-h] option to the program:

  ./aStar_main.py -h


# ---------------------------------------------------------------------------
# Author

Dennis Byington
dennisbyington@mac.com


# ---------------------------------------------------------------------------
# Version History

0.1 - Initial release


# ---------------------------------------------------------------------------
# License

This software is licensed under the MIT License.  See license.txt for details.


# ---------------------------------------------------------------------------
# Acknowledgments

The sites below were instrumental in helping me complete this project:

https://www.javatpoint.com/ai-informed-search-algorithms
https://brilliant.org/wiki/a-star-search/
https://www.baeldung.com/cs/dijkstra-time-complexity
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
http://csis.pace.edu/~benjamin/teaching/cs627/webfiles/Astar.pdf
https://tinypythonprojects.com
https://www.redblobgames.com/pathfinding/
