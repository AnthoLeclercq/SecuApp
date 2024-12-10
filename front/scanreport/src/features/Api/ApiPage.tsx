import { Box, Container, Divider, Grid, Tabs, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useCurrentUser } from "features/Auth/authApi";
import { useDispatch } from "react-redux";
import { colors } from "features/colors";
import logo from "../../images/logo192.png";
import Tab from '@mui/material/Tab';

import HeaderPage from "page/HeaderPage";
import { getRoutes } from "./ApiPageApi";
import { Routes } from "./ApiType";
import RoutesBloc from "./bloc/RoutesBloc";


const ApiPage = () => {
  const dispatch = useDispatch();

  const [routes, setRoutes] = useState<Routes[]>([]);


  function loadRoutes(data: Routes[]){
    if(data){
      setRoutes(data)
    }
  }

  useEffect(() => {
    dispatch<any>(getRoutes(loadRoutes))
  }, []);

  return (
    <Container>
      <Grid container>
        <HeaderPage libelleTxt="API"/>
      </Grid>
      <Grid container mt={2}>
        {routes.map(route => (
          <RoutesBloc route={route} />
        ))}
      </Grid>
    </Container>
  );
}

export default ApiPage;
