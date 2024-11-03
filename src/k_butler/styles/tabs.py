from typing import Optional

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QProxyStyle, QStyle, QStyleOption, QWidget


class CustomTabStyle(QProxyStyle):

    @staticmethod
    def visualAlignment(direction, alignment):
        return super().visualAlignment(direction, alignment)

    def drawComplexControl(self, control, option, painter, widget=...):
        super().drawComplexControl(control, option, painter, widget)

    def sizeFromContents(
            self,
            content_type: QStyle.ContentsType,
            option: Optional[QStyleOption],
            size: QSize,
            widget: Optional[QWidget]) -> QSize:
        size = super().sizeFromContents(content_type, option, size, widget)
        # size.transpose()
        # if isinstance(content_type,  QStyle.::CT_TabBarTab) (
        #
        # )
        return size

    def drawItemPixmap(self, painter, rect, alignment, pixmap):
        super().drawItemPixmap(painter, rect, alignment, pixmap)

    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole=...):
        super().drawItemText(painter, rect, flags, pal, enabled, text, textRole)

    def drawControl(
            self,
            element: QStyle.ControlElement,
            option: Optional[QStyleOption],
            painter: Optional[QPainter],
            widget: Optional[QWidget] = None):
        print(1)
        super().drawControl(element, option, painter, widget)

#   def sizeFromContents_(ContentsType type, const QStyleOption* option,
#                          const QSize& size, const QWidget* widget) const {
#     QSize s = QProxyStyle::sizeFromContents(type, option, size, widget);
#     if (type == QStyle::CT_TabBarTab) {
#       s.transpose();
#     }
#     return s;
#   }
#
#   void drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const {
#     if (element == CE_TabBarTabLabel) {
#       if (const QStyleOptionTab* tab = qstyleoption_cast<const QStyleOptionTab*>(option)) {
#         QStyleOptionTab opt(*tab);
#         opt.shape = QTabBar::RoundedNorth;
#         QProxyStyle::drawControl(element, &opt, painter, widget);
#         return;
#       }
#     }
#     QProxyStyle::drawControl(element, option, painter, widget);
#   }
# };
