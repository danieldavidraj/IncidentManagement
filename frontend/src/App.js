import {
  BrowserRouter as Router,
  useRoutes,
} from "react-router-dom";
import Auth from './component/Auth';
import Incident from './component/Incident';

const App = () => {
  let routes = useRoutes([
    { path: "/", element: <Auth /> },
    { path: "/incidents", element: <Incident /> },
  ]);
  return routes;
};

const AppWrapper = () => {
  return (
    <Router>
      <App />
    </Router>
  );
};

export default AppWrapper;
