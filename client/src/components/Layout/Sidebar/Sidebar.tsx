import React, { ReactElement, useContext } from 'react';
import { Nav, Offcanvas } from 'react-bootstrap';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { NavItem } from 'src/components/Layout/Nav/NavItem';
import { NavSection } from 'src/components/Layout/Nav/NavSection';
import { NavContext, NavContextProps } from 'src/components/Layout/Root';
import { RootState } from 'src/store';
import { routes } from './SidebarRoutes';

/** Vertical sidebar for navigation that disappears when the viewport is small*/
export function Sidebar(): ReactElement | null {
  const authUser = useSelector((state: RootState) => state.auth.user);
  const { showSidebar, setShowSidebar } = useContext<NavContextProps>(NavContext);

  if (!authUser) return null;
  return (
    <Offcanvas show={showSidebar} onHide={setShowSidebar}>
      <Offcanvas.Header closeButton>
        <Offcanvas.Title>
          <Link to="/" className="navbar-brand ps-1 mb-0">
            {/*<img*/}
            {/*  src={logo}*/}
            {/*  alt="haztrak logo, hazardous waste tracking made easy."*/}
            {/*  width={200}*/}
            {/*  height={'auto'}*/}
            {/*/>*/}
          </Link>
        </Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body>
        <nav className="sb-sidenav" id="sidenavAccordion">
          <Nav className="flex-column">
            {routes.map((route) => {
              if (typeof route === 'object' && 'routes' in route) {
                return <NavSection key={route.id} section={route} />;
              } else if (typeof route === 'object' && 'url' in route) {
                return <NavItem key={route.id} route={route} />;
              }
            })}
          </Nav>
        </nav>
      </Offcanvas.Body>
    </Offcanvas>
  );
}
