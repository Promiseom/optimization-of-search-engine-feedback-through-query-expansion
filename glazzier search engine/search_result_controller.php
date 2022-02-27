<?php
    require_once("custom_search.php");

    if($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['search_query'])){
        $page = 1;
        if(isset($_GET['page'])){
            $page = htmlentities($_GET['page']);
        }

        $searchQuery = htmlentities($_GET['search_query']);

        if(empty($searchQuery)){
            echo("invalid query, query cannot be empty");
        }else{
            # search internet with query
            $response = customSearch($searchQuery, $page);
            //echo($response);
            $searchResult = json_decode($response);
            if($searchResult->status_code == 200){
                $searchQuery = $searchResult->message->query;
                $resultItems = $searchResult->message->items;
            }else{
                header("Location: error.html?query=".$searchQuery.'&response='.$response);
                exit();
            }
        }
    }else{
        echo("received post request");
    }
?>