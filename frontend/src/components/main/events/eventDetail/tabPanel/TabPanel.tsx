/**
 * Tab panel for EventDetail component
 */

import React from "react";

import Box from "@material-ui/core/Box";
import Typography from "@material-ui/core/Typography";

import useStyles from "../styles";

interface TabPanelProps {
  children?: React.ReactNode;
  dir?: string;
  index: any;
  value: any;
}

function TabPanel(props: TabPanelProps) {
  const classes = useStyles();
  const { children, value, index, ...other } = props;

  return (
    <Typography
      className={classes.tabPanel}
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`event-detail-tabpanel-${index}`}
      aria-labelledby={`event-detail-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

export default TabPanel;
