#4
<p>Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Example</span></p>
<p>For <code>inputArray = [3, 6, -2, -5, 7, 3]</code>, the output should be<br>
<code>adjacentElementsProduct(inputArray) = 21</code>.</p>
<p><code>7</code> and <code>3</code> produce the largest product.</p>

#5
Below we will define an <code>n</code>-interesting polygon. Your task is to find the area of a polygon for a given <code>n</code>.</p>
<p>A <code>1</code>-interesting polygon is just a square with a side of length <code>1</code>. An <code>n</code>-interesting polygon is obtained by taking the <code>n - 1</code>-interesting polygon and appending <code>1</code>-interesting polygons to its rim, side by side. You can see the <code>1</code>-, <code>2</code>-, <code>3</code>- and <code>4</code>-interesting polygons in the picture below.</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Example</span></p>
<ul>
<li>For <code>n = 2</code>, the output should be<br>
<code>shapeArea(n) = 5</code>;</li>
<li>For <code>n = 3</code>, the output should be<br>
<code>shapeArea(n) = 13</code>.</li>
<img src="www.imgur.com/a/st6X0Ex">

#6
Ratiorg got <code>statues</code> of <em>different</em> sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by <code>1</code>. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Example</span></p>
<p>For <code>statues = [6, 2, 3, 8]</code>, the output should be<br>
<code>makeArrayConsecutive2(statues) = 3</code>.</p>
<p>Ratiorg needs statues of sizes <code>4</code>, <code>5</code> and <code>7</code>.</p>

#7
<p>Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.</p>
<p><em>Note:</em> sequence <code>a<sub>0</sub></code>, <code>a<sub>1</sub></code>, ..., <code>a<sub>n</sub></code> is considered to be a strictly increasing if <code>a<sub>0</sub> &lt; a<sub>1</sub> &lt; ... &lt; a<sub>n</sub></code>. Sequence containing only one element is also considered to be strictly increasing.</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Example</span></p>
<ul>
<li>
<p>For <code>sequence = [1, 3, 2, 1]</code>, the output should be<br>
<code>almostIncreasingSequence(sequence) = false</code>.</p>
<p>There is no one element in this array that can be removed in order to get a strictly increasing sequence.</p>
</li>
<li>
<p>For <code>sequence = [1, 3, 2]</code>, the output should be<br>
<code>almostIncreasingSequence(sequence) = true</code>.</p>
<p>You can remove <code>3</code> from the array to get the strictly increasing sequence <code>[1, 2]</code>. Alternately, you can remove <code>2</code> to get the strictly increasing sequence <code>[1, 3]</code>.</p>

#8
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, <strong>or any of the rooms below any of the free rooms</strong>.</p>
<p>Given <code>matrix</code>, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a <code>0</code>).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
</code></pre>
<p>the output should be<br>
<code>matrixElementsSum(matrix) = 9</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/matrixElementsSum/img/example1.png?_tm=1551538346086" alt="example 1"></p>
<p>There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is <code>1 + 5 + 1 + 2 = 9</code>.</p>
