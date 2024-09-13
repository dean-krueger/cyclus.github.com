.. _dbtypes:

Database Types
==============

Here is a listing of all supported data types that the various backends have
implemented, by |cyclus| version number. If your agents need a type that is not
yet supported, please let us know and we'll get to it as soon as possible!

**Description of fields:**

:ID: Enum identifier (value) for database type in the ``cyclus::DbTypes`` enum.
:Name: Enum name for database type in the ``cyclus::DbTypes`` enum.
:C++ Type: The corresponding C++ type.
:Shape Rank: The maximum rank (length) of the ``shape`` vector.
:Backend: The database backend type.
:Version: The |cyclus| version.
:Supported: Flag for if the backend supported this type in this release.

.. raw:: html

    <br />

    <link rel="stylesheet" href="../_static/pivot/datatables-2.1.6.min.css" type="text/css" />
    <link rel="stylesheet" href="../_static/cyclus.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />

    <style>
    p {
      font-size: 100%;
    }

    img {
      max-height: 100px;
    }

    img.logo {
      max-height: none;
    }
    </style>

    <!-- jquery_pivot must be loaded after pivot.js and jQuery -->
    <script type="text/javascript" src="../_static/pivot/jquery-3.7.1.min.js"></script>
    <script type="text/javascript" src="../_static/pivot/datatables-2.1.6.min.js"></script>

    <script type="text/javascript">
    var dbdata = []
    $.getJSON("/arche/dbtypes.json", function(json) {
        // this mapping is purely for formatting purposes
        dbdata = json.map(function(row){
          let formattedRow = [ ...row ]
          formattedRow[6] = row[6] === 1 ? "True" : "False"; // change supported flag to a string
          formattedRow[5] = row[5].startsWith('v') ? row[5] : "v" + row[5]; // add a 'v' prefix to the version number if it doesn't exist
          return formattedRow;
        });

        $(document).ready(function() {
            $('#dbtypes-table').DataTable({
              data: dbdata.slice(1),
              paging: true,
              pageLength: 25,
              scrollX: true,
              autoWidth: true,
              order: [
                { idx: 5, dir: 'desc' }, // sort by version first
                { idx: 0, dir: 'asc' }, // sort by id
              ],
              columns: [
                { title: "ID", searchable: true },
                { title: "Name", searchable: true },
                { title: "C++ Type", searchable: true },
                { title: "Shape Rank",},
                { title: "Backend", searchable: true },
                { title: "Version", searchable: true },
                { title: "Supported", },
              ]
            })

        });
    });

    </script>


    <table id="dbtypes-table" class="display">
      <!-- table content will be dynamically populated by the javascript above -->
    </table>