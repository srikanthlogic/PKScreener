window.addEventListener('load', function() {
  if (document.getElementsByTagName("TR")[1].firstElementChild.innerText === 'Stock') {
    /*Get rid of the first row with Stocks on all columns*/
    document.getElementsByTagName("TR")[1].remove()
  }
  const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;
  const chkBox = document.getElementById('chkActualNumbers')
  const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
      v1 !== '' && v2 !== '' && !isNaN(parseFloat(v1)) && !isNaN(parseFloat(v2)) ? ((chkBox && chkBox.checked && v1.split('(').length > 1)? (parseFloat(v1.replaceAll("/","").split('(')[1].split(')')[0]) - parseFloat(v2.replaceAll("/","").split('(')[1].split(')')[0])):(parseFloat(v1.replaceAll("/","")) - parseFloat(v2.replaceAll("/","")))): v1.toString().localeCompare(v2)
      )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

  // do the work...
  document.querySelectorAll('th').forEach(th => th.addEventListener('click', (() => {
      var table = th.closest('table');
      const tbody = table.querySelector('tbody');
      Array.from(tbody.querySelectorAll('tr'))
          .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
          .forEach(tr => tbody.appendChild(tr) );
  })));
})