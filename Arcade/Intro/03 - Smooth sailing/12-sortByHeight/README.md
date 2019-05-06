<div class="markdown"><p>Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Example</span></p>
<p>For <code>a = [-1, 150, 190, 170, -1, -1, 160, 180]</code>, the output should be<br>
<code>sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]</code>.</p>
<p><span style="color:#44BFA3;font-size:1.4em;">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>If <code>a[i] = -1</code>, then the <code>i<sup>th</sup></code> position is occupied by a tree. Otherwise <code>a[i]</code> is the height of a person standing in the <code>i<sup>th</sup></code> position.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ a.length ≤ 1000</code>,<br>
<code>-1 ≤ a[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<ul>
<li>Sorted array <code>a</code> with all the trees untouched.</li>
</div>