from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from libs.baseclass.transformXYZ import transformXYZ


class Home(Screen):

    with open('libs/kv/home.kv', 'r', encoding='utf-8') as home_kv:
        Builder.load_string(home_kv.read())
    
    def transforming(self, x0, y0, z0, t0, tp, dx, dy, dz, wx, wy, wz, m, ux, uy, uz, t2):
        x0, y0, z0 = float(x0), float(y0), float(z0)
        dx, dy, dz, wx, wy, wz, m = float(dx), float(dy), float(dz), float(wx), float(wy), float(wz), float(m)
        ux, uy, uz = float(ux), float(uy), float(uz)
        
        tp = int(tp.split('-')[0]) + int(tp.split('-')[1])/12 + int(tp.split('-')[2])/365
        t0 = int(t0.split('-')[0]) + int(t0.split('-')[1])/12 + int(t0.split('-')[2])/365
        t2 = int(t2.split('-')[0]) + int(t2.split('-')[1])/12 + int(t2.split('-')[2])/365
        dt1, dt2 = abs(tp-t0), abs(t2-tp)
        print(dt1, type(dt1))
        print(dt2, type(dt2))
        x0 += dt1*ux
        y0 += dt1*uy
        z0 += dt1*uz
        k_res = transformXYZ(x0, y0, z0, dx, dy, dz, wx, wy, wz, m)
        x2 = float(k_res[0][0]) + dt2*ux
        y2 = float(k_res[1][0]) + dt2*uy
        z2 = float(k_res[2][0]) + dt2*uz
        self.ids.x2.text = str(round(x2, 3))
        self.ids.y2.text = str(round(y2, 3))
        self.ids.z2.text = str(round(z2, 3))


class TranscorCalcApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))

        return sm


if __name__ == "__main__":
    TranscorCalcApp().run()